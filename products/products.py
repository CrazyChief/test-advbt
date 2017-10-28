from django.conf import settings
from django.http import JsonResponse
from django.db.models import Max
from .models import ProductVariation

session_key = getattr(settings, 'PRODUCT_SESSION_KEY', 'products')


class ProductBase(object):

    default_min_price = 10
    default_max_price = int(ProductVariation.objects.all().aggregate(Max('price'))['price__max'])
    # default_max_price = 100

    def __init__(self, request):
        self.request = request
        self.session = self.request.session
        session_data = request.session.setdefault(session_key, {})
        self.min_price = session_data.get('min_price', self.default_min_price)
        self.max_price = session_data.get('max_price', self.default_max_price)

    def set_price_values(self, min_price, max_price):
        self.min_price = min_price
        self.max_price = max_price
        self.update()

    def get_price_values(self):
        return {
            'min_price': self.min_price,
            'max_price': self.max_price,
        }

    def encode(self):
        price_repr = {
            'min_price': self.min_price,
            'max_price': self.max_price,
        }
        return JsonResponse(price_repr)

    def update(self):
        session = self.request.session
        session_data = session[session_key]
        session_data['min_price'] = self.min_price
        session_data['max_price'] = self.max_price
        session.modified = True

    def reset(self):
        return self.set_price_values(self.default_min_price, self.default_max_price)
