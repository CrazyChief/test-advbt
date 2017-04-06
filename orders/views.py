from django.shortcuts import render
from easycart import BaseCart
from django.http import HttpResponseForbidden
from django.views.generic import FormView
from .forms import OrderCreateForm
from .models import Order, OrderItem
from products.models import ProductVariation
from cart.views import Cart


class CheckoutView(FormView):
    template_name = 'orders/checkout.html'
    form_class = OrderCreateForm
    success_url = '/thanks/'

    def __init__(self):
        self.cart = Cart

    def get(self, request, *args, **kwargs):
        self.cart = self.cart(request)
        # print(self.cart.list_items())
        # self.li = self.cart.list_items()
        return super(CheckoutView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request:
            return HttpResponseForbidden()
        form = self.get_form()
        print(form)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        order = form.save()
        for item in self.cart.list_items(Cart(self.request)):
            OrderItem.objects.create(order=order, product=item.obj, price=item.obj.price, quantity=item.quantity)
            ProductVariation.objects.get(pk=item.obj.pk).update_quantity(item.quantity)
        self.cart.empty(Cart(self.request))
        return super(CheckoutView, self).form_valid(form)



