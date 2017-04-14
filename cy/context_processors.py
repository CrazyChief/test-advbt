from django.conf import settings
from .cy import CY

session_key = getattr(settings, 'CURRENCY_SESSION_KEY', 'currency')


def currency(request):
    return {'currency': CY(request)}


