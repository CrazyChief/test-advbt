from django.shortcuts import render, get_object_or_404
from decimal import Decimal
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from cart.views import Cart
from orders.models import Order


def PaymentProcess(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    amount = Decimal(request.session.get('easycart').get('totalPrice'))
    host = request.get_host()

    paypal_dict = {
        'business': 'danilovdmitry94-facilitator-1@gmail.com',
        # 'amount': '%.2f' % amount.quantize(Decimal('.01')),
        'amount': '100.00',
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://2f6da08b.ngrok.io' + reverse('paypal-ipn'),
        'return_url': 'http://2f6da08b.ngrok.io' + reverse('payment:done'),
        'cancel_return': 'http://2f6da08b.ngrok.io' + reverse('payment:canceled')
    }
    print(paypal_dict)
    # paypal_dict = {
    #     'business': 'danilovdmitry94-facilitator@gmail.com',
    #     'amount': '100.00',
    #     'item_name': '1',
    #     'invoice': '1',
    #     # 'currency_code': 'USD',
    #     'notify_url': 'http://2f6da08b.ngrok.io' + reverse('paypal-ipn'),
    #     'return_url': 'http://2f6da08b.ngrok.io' + reverse('payment:done'),
    #     'cancel_return': 'http://2f6da08b.ngrok.io' + reverse('payment:canceled')
    # }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {
        'order': order,
        'form': form,
    }
    return render(request, 'payment/process.html', context)


from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from payment.signals import payment_notification
from orders.models import Order


# print("We in signals file. Defining of function")


# def payment_notification(sender, **kwargs):
#     ipn_obj = sender
#     print(sender)
#     if ipn_obj['payment_status'] == ST_PP_COMPLETED:
#         print("Order completed! :)")
#         print("PK: %s" % ipn_obj['invoice'])
#         if ipn_obj['receiver_email'] != 'seller@paypalsandbox.com':
#         # 'danilovdmitry94-facilitator-1@gmail.com'
#             print("No receiver email! :(")
#             return
#
#         order = get_object_or_404(Order, pk=ipn_obj['invoice'])
#         # if order is not None:
#         print(order)
#         order.pay_status = True
#         order.save()

# print("We defined function.")
# valid_ipn_received.connect(payment_notification)
# print("We awake our function!)")


@csrf_exempt
def PaymentDone(request):
    valid_ipn_received.connect(payment_notification)
    print(request.POST)
    cart = Cart(request)
    cart.empty()
    return render(request, 'payment/done.html')


@csrf_exempt
def PaymentCanceled(request):
    return render(request, 'payment/canceled.html')
