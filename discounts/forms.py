from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Discount


class DiscountApplyForm(ModelForm):
    class Meta:
        model = Discount
        fields = ['discount_code']

    def __init__(self, *args, **kwargs):
        super(DiscountApplyForm, self).__init__(*args, **kwargs)
        self.fields['discount_code'].widget.attrs.update({
            'placeholder': _('Code'),
        })
