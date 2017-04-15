from django.db import models
from django.utils.translation import ugettext_lazy as _


class Cy(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('Name'))
    abbreviation = models.CharField(max_length=6, unique=True, verbose_name=_('Abbreviation'))
    symbol = models.CharField(max_length=1, unique=True, verbose_name=_('Symbol'))
    dimension = models.DecimalField(max_digits=19, decimal_places=10, verbose_name=_('Dimension'))
    base = models.BooleanField(default=False, verbose_name=_('Base'))
    active = models.BooleanField(default=False, verbose_name=_('Active'))

    class Meta:
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')

    def __str__(self):
        return self.symbol + " (" + self.abbreviation + ")"

    def is_active(self):
        return self.active

    is_active.admin_order_field = 'active'
    is_active.boolean = True
    is_active.short_description = _('Is active?')

