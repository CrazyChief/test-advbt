from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from orders.models import Order


print("We in signals file. Defining of function")


def payment_notification(sender, **kwargs):
    ipn_obj = sender
    print(sender)
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        print("Order completed! :)")
        print("PK: %s" % ipn_obj.invoice)
        if ipn_obj.receiver_email != 'danilovdmitry94-facilitator-1@gmail.com':
            print("No receiver email! :(")
            return

        order = get_object_or_404(Order, pk=ipn_obj.invoice)
        # if order is not None:
        print(order)
        order.pay_status = True
        order.save()

print("We defined function.")
valid_ipn_received.connect(payment_notification)
print("We awake our function!)")
