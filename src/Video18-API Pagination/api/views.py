from django.db.models import Max
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProductSerializer, OrderSerializer, ProductInfoSerializer
from .models import Product, Order, OrderItem
from .filter import ProductFilter, InStockFilter


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    # pagination_class = PageNumberPagination
    # pagination_class.page_size=3
    # pagination_class.page_query_param='page_num'
    # pagination_class.page_size_query_param='s'
    # pagination_class.max_page_size=6
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


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related("items__product")
    serializer_class = OrderSerializer


class UserOrderListView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related("items__product")
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


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
