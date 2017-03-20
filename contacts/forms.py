from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'name',
            'email',
            'review',
        ]
        labels = {
            'review': _('Message')
        }



















