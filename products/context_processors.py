from django.conf import settings
from .models import Product, ProductVariation
from .products import ProductBase


def product(request):
    return {'product': ProductBase(request)}

