from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_added',)
    list_filter = ['date_added',]


admin.site.register(Subscriber, SubscriberAdmin)
