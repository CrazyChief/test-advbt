from django.conf import settings
from django.views.generic import View, DetailView
# from django.urls import reverse
from django.http import HttpResponseRedirect
# from .cy import CY
from .conf import session_key
from .models import Cy


class CyView(View):
    template_name = 'currency/currency_base_template.html'

    def get(self, request):
        currency_abbreviation = self.request.GET.get('currency_abbreviation')

        response = HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        if currency_abbreviation and Cy.objects.filter(abbreviation=currency_abbreviation).exists():
            if hasattr(request, 'session'):
                print("yeah")
                self.request.session[session_key] = currency_abbreviation
            else:
                print('no')
                response.set_cookie(session_key, currency_abbreviation)
        print("Response from view: %s" % self.request.session[session_key])
        return response



