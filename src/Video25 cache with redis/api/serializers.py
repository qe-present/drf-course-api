from rest_framework import serializers
from django.db import transaction
from .models import Product, Order, OrderItem, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("password", "user_permissions", "is_authenticated",'get_full_name','orders')



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "stock",
        )

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name")
    product_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, source="product.price"
    )

    class Meta:
        model = OrderItem
        fields = ("product_name", "product_price", "quantity", "item_subtotal")


class OrderSerializer(serializers.ModelSerializer):
    order_id = serializers.UUIDField(read_only=True)
    items = OrderItemSerializer(many=True)
    total_price = serializers.SerializerMethodField(method_name="total")

    def total(self, obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)

    class Meta:
        model = Order
        fields = (
            "order_id",
            "created_at",
            "user",
            "status",
            "items",
            "total_price",
        )


class OrderCreateSerializer(serializers.ModelSerializer):
    class OrderItemCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = OrderItem
            fields = ("product", "quantity")
    def create(self, validated_data):
        """
        {   'user': <User: qe>,
         '  status': 'Pending',
            'items':
            [{'product': <Product: Coffee Machine>, 'quantity': 1},
            {'product': <Product: Velvet Underground & Nico>, 'quantity': 2}]}
        """
        items=validated_data.pop("items")
        with transaction.atomic():
            order=Order.objects.create(**validated_data)
            for item in items:
                OrderItem.objects.create(order=order,**item)
        return order
    def update(self, instance, validated_data):
        items = validated_data.pop("items", None)
        with transaction.atomic():
            instance=super().update(instance, validated_data)

            if items is not None:
                print(instance)
                print(instance.items.all())
                # Clear existing items
                instance.items.all().delete()
                # Add new items
                for item in items:
                    OrderItem.objects.create(order=instance, **item)

        return instance


    items = OrderItemCreateSerializer(many=True,required=False)
    class Meta:
        model = Order
        fields = ("order_id","user", "status", "items")
        extra_kwargs = {"user": {"read_only": True}}




class ProductInfoSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)
    count = serializers.IntegerField()
    max_price = serializers.FloatField()
