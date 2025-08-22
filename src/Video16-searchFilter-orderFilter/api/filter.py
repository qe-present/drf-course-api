import django_filters
from .models import Product


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
