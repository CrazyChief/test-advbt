from django.shortcuts import render, get_object_or_404
from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from orders.models import Order


def PaymentProcess(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    amount = Decimal(request.session.get('easycart').get('totalPrice'))
    host = request.get_host()

    paypal_dict = {
        'business': 'danilovdmitry94-facilitator-1@gmail.com',
        'amount': '%.2f' % amount.quantize(Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'https://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'https://{}{}'.format(host, reverse('payment:done')),
        'cancel_return': 'https://{}{}'.format(host, reverse('payment:canceled'))
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {
        'order': order,
        'form': form,
    }
    return render(request, 'payment/process.html', context)

@csrf_exempt
def PaymentDone(request):

    return render(request, 'payment/done.html')

@csrf_exempt
def PaymentCanceled(request):
    return render(request, 'payment/canceled.html')
