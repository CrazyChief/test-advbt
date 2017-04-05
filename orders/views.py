from django.shortcuts import render
from easycart import BaseCart
from django.http import HttpResponseForbidden
from django.views.generic import FormView
from .forms import OrderCreateForm
from .models import Order, OrderItem
from products.models import ProductVariation


class CheckoutView(FormView):
    template_name = 'orders/checkout.html'
    form_class = OrderCreateForm

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def get(self, request, *args, **kwargs):
        for item in request.session:
            print(item)
        return super(CheckoutView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not request:
            return HttpResponseForbidden()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        pass
        # obj = form.save(commit=False)
        # obj.product = ProductVariation.objects.get(pk=self.kwargs['pk'])
        # obj.save()
        # return super(ProductView, self).form_valid(form)



