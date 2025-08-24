from django.db.models import Max
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.decorators import api_view, action
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .filter import InStockFilter, OrderFilter, ProductFilter
from .models import Order, OrderItem, Product
from .serializers import OrderSerializer, ProductInfoSerializer, ProductSerializer,OrderCreateSerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    pagination_class = LimitOffsetPagination
    filter_backends = [
        # InStockFilter,
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["=name"]
    ordering_fields = ["stock", "price"]

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class ProductAddView(generics.CreateAPIView):
    model = Product
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)

        return super().create(request, *args, **kwargs)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    lookup_url_kwarg = "product_id"

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ["PUT", "DELETE"]:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]
    filterset_class = OrderFilter
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def get_serializer_class(self):
        if self.action=='create':
            return OrderCreateSerializer
        return super().get_serializer_class()


    def get_queryset(self):
        qs=super().get_queryset()
        print(self.request.user.is_staff)
        if not self.request.user.is_staff:
            qs=qs.filter(user=self.request.user)
        return qs

    @action(
        detail=False,
        methods=["get"],
        url_path="user-orders"
    )
    def user_orders(self, request):
        orders = self.get_queryset().filter(user=request.user)
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)


class ProductInfoView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductInfoSerializer(
            {
                "products": products,
                "count": len(products),
                "max_price": products.aggregate(max_price=Max("price"))["max_price"],
            }
        )
        return Response(serializer.data)
