import django_filters
from rest_framework import filters
from .models import Product, Order


class InStockFilter(filters.BaseFilterBackend):
    """
    Filter to return only products that are in stock.
    """

    def filter_queryset(self, request, queryset, view):
        # return queryset.filter(stock__range=(0, 80))
        return queryset.exclude(stock__range=(0, 80))


class ProductFilter(django_filters.FilterSet):
    """
    Filter for Product model.
    """

    class Meta:
        model = Product
        fields = {
            "name": ["exact", "contains"],
            "price": ["exact", "lt", "gt", "range"],
        }


class OrderFilter(django_filters.FilterSet):
    created_at = django_filters.DateTimeFilter(
        field_name="created_at__date",
    )
    """
    Filter for Order model.
    """

    class Meta:
        model = Order
        fields = {
            "status": ["exact"],
            "created_at": ["exact", "lt", "gt"],
        }
