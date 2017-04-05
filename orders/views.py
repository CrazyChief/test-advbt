from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.views.generic import FormView
from .forms import OrderCreateForm


class CheckoutView(FormView):
    template_name = 'orders/checkout.html'
    form_class = OrderCreateForm

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context



    

