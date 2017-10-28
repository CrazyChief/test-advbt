from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import ProductReview, ProductQuestion


class ReviewForm(ModelForm):
    class Meta:
        model = ProductReview
        fields = ['review', 'reviewer_name', 'reviewer_email']
        labels = {
            'reviewer_name': _('Name'),
            'reviewer_email': _('Email'),
        }


class QuestionForm(ModelForm):
    class Meta:
        model = ProductQuestion
        fields = ['question', 'name', 'email']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': _('Name'),
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': _('Email'),
        })
        self.fields['question'].widget.attrs.update({
            'placeholder': _('Question'),
        })


