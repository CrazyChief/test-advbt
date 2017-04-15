from .models import Cy
from django.conf import settings
from .conf import session_key
# from .utils import get_active_currency


def currency(request):
    if not session_key in request.session or request.session.get(session_key) is None:
        request.session[session_key] = Cy.objects.get(base__exact=True).abbreviation

    try:
        cy = Cy.objects.get(abbreviation__iexact=request.session[session_key])
    except Cy.DoesNotExist:
        cy = None
    print("From context processor: %s" % cy)
    return {
        'CURRENCIES': Cy.objects.filter(active=True),
        'CURRENCY_ACTIVE': cy,
    }


