from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import ProductReview, ProductAnswer


class ReviewForm(ModelForm):
    class Meta:
        model = ProductReview
        fields = ['review', 'reviewer_name', 'reviewer_email']
        labels = {
            'reviewer_name': _('Name'),
            'reviewer_email': _('Email'),
        }


class AnswerForm(ModelForm):
    class Meta:
        model = ProductAnswer
        fields = ['answer', 'name', 'email']

















