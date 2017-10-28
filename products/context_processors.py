from .products import ProductBase


def product(request):
    return {'product': ProductBase(request)}

