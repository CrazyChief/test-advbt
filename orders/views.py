from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.views.generic import FormView, DetailView
from .forms import OrderCreateForm
from .models import Order, OrderItem
from cart.views import Cart
from .tasks import OrderCreated
from products.models import Category
from templated_email import send_templated_mail


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
        context['category_list'] = Category.objects.filter(is_active=True)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request:
            return HttpResponseForbidden()
        form = self.get_form()
        # print(form)
        if form.is_valid():
            self.order = form.save(commit=False)
            self.order.save()
            for item in self.cart.list_items(Cart(self.request)):
                OrderItem.objects.create(order=self.order, product=item.obj, price=item.obj.price,
                                         quantity=item.quantity)
            if self.order.pay_type == "N":
                self.request.session['order_id'] = self.order.id
                # self.cart.empty(Cart(self.request))
                return redirect(reverse('payment:process'))
            elif self.order.pay_type == "W_R":
                send_templated_mail(
                    template_name='order',
                    from_email='noreply@sandbox8f86f5175eec47f39c7887ee6e45e3a9.mailgun.org',
                    recipient_list=[self.order.shipping_email],
                    context={
                        'order': self.order,
                    }
                )
                self.cart.empty(Cart(self.request))
                return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)

    # def form_valid(self, form):
    #     self.order = form.save(commit=False)
    #     for item in self.cart.list_items(Cart(self.request)):
    #         OrderItem.objects.create(order=self.order, product=item.obj, price=item.obj.price, quantity=item.quantity)
    #         # ProductVariation.objects.get(pk=item.obj.pk).update_quantity(item.quantity)
    #         # OrderCreated.delay(self.order.id)
    #     self.request.session['order_id'] = self.order.id
    #     self.cart.empty(Cart(self.request))
    #     redirect(reverse('payment:process'))
    #     return super(CheckoutView, self).form_valid(form)

    def get_success_url(self):
        # return redirect(reverse('payment:process'))
        return reverse('orders:created', kwargs={'pk': self.order.pk})


class CreatedView(DetailView):
    model = Order
    template_name = 'orders/created.html'

    # def __init__(self):
    #     self.order = OrderCreated

    # def get(self, request, *args, **kwargs):
    #     self.order(kwargs['pk'])
    #     return super(CreatedView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreatedView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.filter(is_active=True)
    #     context['ord'] = OrderCreate(kwargs['pk'])
        return context

