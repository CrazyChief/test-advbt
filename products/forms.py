from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import ProductReview


class ReviewForm(ModelForm):
    class Meta:
        model = ProductReview
        fields = ['review', 'reviewer_name', 'reviewer_email']
        labels = {
            'reviewer_name': _('Name'),
            'reviewer_email': _('Email'),
        }


















