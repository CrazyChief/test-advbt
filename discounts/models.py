import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import ugettext_lazy as _


class Discount(models.Model):
    """
    Discount model. Stores an information about discount in details
    """
    PER_PRODUCT = 'P_P'
    FOR_ALL = 'F_A'
    # TYPES = (
    #     (PER_PRODUCT, 'Per product'),
    #     (FOR_ALL, 'For all'),
    # )
    TYPES = (
        (FOR_ALL, 'Coupon'),
    )
    discount_title = models.CharField(max_length=200, verbose_name=_('Title'))
    discount_code = models.CharField(max_length=20, verbose_name=_('Code'))
    discount_range = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name=_('Range'))
    discount_type = models.CharField(max_length=20, choices=TYPES, default=FOR_ALL, verbose_name=_('Title'))
    # discount_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    discount_start_period = models.DateTimeField(verbose_name=_('Start period'))
    discount_end_period = models.DateTimeField(verbose_name=_('End period'))
    discount_description = models.TextField(verbose_name=_('Description'))

    class Meta:
        verbose_name = _("Discount")
        verbose_name_plural = _("Discounts")

    def __str__(self):
        return "%s %s" % (self.discount_code, self.discount_type)

    def out_of_date(self):
        now = timezone.now()
        return self.discount_end_period <= now

    out_of_date.admin_order_field = 'discount_end_period'
    out_of_date.boolean = True
    out_of_date.short_description = 'Is out of date?'
