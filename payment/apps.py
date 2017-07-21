from django.apps import AppConfig


class PaymentConfig(AppConfig):
    name = 'payment'
    verbose_name = 'Payment'

    def ready(self):
        # print("Payment app is ready!")
        import payment.signals
        # print("I hope, It imported!")
