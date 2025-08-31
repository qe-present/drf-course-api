from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from .models import Product
from django.core.cache import cache


@receiver([post_delete,post_save], sender=Product)
def validate_product_list(sender, instance, created, **kwargs):
    print("clear product list cache")
    cache.delete_pattern("*product_list*")