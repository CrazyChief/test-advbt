from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from django.conf import settings
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from orders.models import Order
from templated_email import send_templated_mail


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn_obj = sender
    # print("Sender %s" % sender)
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # print("Order completed! :)")
        # print("PK: %s" % ipn_obj.invoice)
        if ipn_obj.receiver_email != settings.PAYPAL_RECEIVER_EMAIL:
            # print("No receiver email! :(")
            return

        order = get_object_or_404(Order, pk=ipn_obj.invoice)
        # if order is not None:
        # print(order)
        order.pay_status = True
        order.save()

        send_templated_mail(
            template_name='order',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[order.shipping_email],
            context={
                'order': order,
            }
        )


