from django.shortcuts import render, get_object_or_404
from decimal import Decimal
from django.core.urlresolvers import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from cart.views import Cart
from orders.models import Order


@csrf_exempt
def PaymentDone(request):
    cart = Cart(request)
    cart.empty()
    return render(request, 'payment/done.html')


@csrf_exempt
def PaymentCanceled(request):
    return render(request, 'payment/canceled.html')


def PaymentProcess(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    amount = Decimal(request.session.get('easycart').get('totalPrice'))
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % amount.quantize(Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled'))
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {
        'order': order,
        'form': form,
    }
    return render(request, 'payment/process.html', context)
