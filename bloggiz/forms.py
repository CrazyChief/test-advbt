from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Comments


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'comment']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': _('Name'),
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': _('Email'),
        })
        self.fields['comment'].widget.attrs.update({
            'placeholder': _('Comment'),
        })
