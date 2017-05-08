from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.http import HttpResponse


class Subscriber(models.Model):
    name = models.CharField(max_length=240, verbose_name=_('Name'))
    email = models.EmailField(max_length=240, unique=True, verbose_name=_('Email'))
    date_added = models.DateTimeField(auto_now_add=True, verbose_name=_('Date of creation'))

    class Meta:
        ordering = ['-date_added']
        verbose_name = _('Subscriber')
        verbose_name_plural = _('Subscribers')

    def get_absolute_url(self):
        return HttpResponse

    def __str__(self):
        return self.name
