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

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': _('Name'),
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': _('Email'),
        })
        self.fields['review'].widget.attrs.update({
            'placeholder': _('Message'),
        })



















