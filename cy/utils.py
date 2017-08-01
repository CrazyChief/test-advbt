from decimal import Decimal as D, ROUND_UP
from .models import Cy
from .conf import session_key


def calc(price, abbreviation, decimals=2):
    dimension = Cy.objects.get(abbreviation__iexact=abbreviation).dimension
    price = (D(price)) * dimension
    return price_round(price, decimals=decimals)


def get_active_currency(request):
    for attr in ('session', 'COOKIES'):
        if hasattr(request, attr):
            try:
                return Cy.objects.get(abbreviation__iexact=getattr(request, attr)[session_key])
            except KeyError:
                continue

    try:
        return Cy.objects.get(base=True)
    except Cy.DoesNotExist:
        return None


def price_round(price, decimals=2):
    decimal_f = "0.1"
    if decimals > 1:
        decimal_f = "0.{}".format('1'.zfill(decimals))
    return price.quantize(D(decimal_f), rounding=ROUND_UP)
