from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def OrderCreated(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Order with number {}'.format(order.id)
    message = """Dear, {}, you have successfully placed an order.\n
                Your order number is {}""".format(order.shipping_first_name, order.id)
    mail_send = send_mail(subject, message, 'info@adavibeauty.com', [order.shipping_email])
    return mail_send









