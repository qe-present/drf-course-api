from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductListView.as_view()),
    path("products/info/", views.ProductInfoView.as_view()),
    path("products/<int:product_id>/", views.ProductDetailView.as_view()),
    path("orders/", views.OrderListView.as_view()),
    path("user-orders/", views.UserOrderListView.as_view(), name="uo"),
]
