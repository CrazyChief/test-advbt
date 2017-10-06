from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.conf import settings
from django.core import mail
from django.views.generic.edit import CreateView

from templated_email import send_templated_mail, get_templated_mail

from .models import Subscriber


class SubscriberView(object):
    """Base class for views operating the subscribers."""
    action = None
    required_params = {}
    """Iterable of parameters, which MUST be present in the post data."""

    # def get(self, request):
    #     return super(SubscriberView, self).get(request)
    #
    # def post(self, request):
    #     params = {}
    #     for param in self.required_params:
    #         try:
    #             params[param] = request.POST[param]
    #         except KeyError:
    #             return JsonResponse({
    #                 'error': 'MissingRequestParam',
    #                 'param': param,
    #             })
    #         print(request.POST[param])
    #     return JsonResponse

    def form_invalid(self, form):
        response = super(SubscriberView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(SubscriberView, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'email': self.object.email,
                'name': self.object.name,
            }
            print(data)
            send_templated_mail(
                template_name='subscriber_noreply',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[self.object.email],
                context={
                    'full_name': self.object.name,
                }
            )
            send_templated_mail(
                template_name='new_subscriber',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                context={
                    'full_name': self.object.name,
                    'email': self.object.email,
                }
            )
            # msg = """Dear %s, thanks for your subscribing. We will notify you about all news on our site.
            # Regards, AdaviBeauty.""" % self.object.name
            # with mail.get_connection() as connection:
            #     mail.EmailMessage(
            #         "No reply, AdaviBeauty", msg, settings.DEFAULT_FROM_EMAIL, [self.object.email],
            #         connection=connection
            #     ).send()
            return JsonResponse(data)
        else:
            return response


class AddSubscriber(SubscriberView, CreateView):
    action = 'add'
    model = Subscriber
    fields = ['email', 'name']
    # required_params = {
    #     'email',
    #     'name',
    # }
