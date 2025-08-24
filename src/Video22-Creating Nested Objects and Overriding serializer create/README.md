# 运行
```bash
rye run dev
```

# 迁移
```shell
python manage.py makemigrations;
python manage.py migrate;
```

# The `.create()` method does not support writable nested fields by default.
# Write an explicit `.create()` method for serializer `api.serializers.OrderCreateSerializer`, or set `read_only=True` on nested serializer fields.
这是因为默认情况下，Django REST Framework 的 .create() 方法不支持嵌套的可写字段。
你需要为 OrderCreateSerializer 编写一个自定义的 .create() 方法，以便在保存订单时正确处理嵌套的订单项
```python
    def create(self, validated_data):
        """
        {   'user': <User: qe>,
         '  status': 'Pending',
            'items':
            [{'product': <Product: Coffee Machine>, 'quantity': 1},
            {'product': <Product: Velvet Underground & Nico>, 'quantity': 2}]}
        """
        items=validated_data.pop("items")
        order=Order.objects.create(**validated_data)
        for item in items:
            OrderItem.objects.create(order=order,**item)
        return order
```