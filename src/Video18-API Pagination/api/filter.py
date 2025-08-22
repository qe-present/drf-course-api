import django_filters
from rest_framework import filters
from .models import Product


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
