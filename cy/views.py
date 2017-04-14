from django.conf import settings
from django.views.generic import View, DetailView
# from django.urls import reverse
from django.http import HttpResponseRedirect
from .cy import CY
from .context_processors import session_key
from .models import Cy


class CyView(View):
    template_name = 'currency/currency_base_template.html'

    def get(self, request):
        # self.request = request
        cy = CY(request)
        # print(self.request.GET.get('currency_abbreviation'))
        # print(self.request.session[session_key])
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

    # def get_context_data(self, **kwargs):
    #     context = super(CyView, self).get_context_data(**kwargs)
    #     context['CURRENCIES'] = Currency.objects.filter(active=True)
    #     return context

    # def post(self, request):
    #     pass