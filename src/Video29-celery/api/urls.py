from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path("products/", views.ProductListView.as_view()),
    path("products/add", views.ProductAddView.as_view()),
    path("products/info/", views.ProductInfoView.as_view()),
    path("products/<int:product_id>/", views.ProductDetailView.as_view(),name="product-detail"),
    path("users/",views.UserListView.as_view())
]
router = DefaultRouter()
router.register("orders", views.OrderViewSet)
urlpatterns += router.urls
