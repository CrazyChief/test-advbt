# from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'comment', 'parent']
        # user = forms.IntegerField(widget=forms.HiddenInput, required=False)
        # parent = forms.IntegerField(widget=forms.HiddenInput, required=False)

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
        # self.fields['user'] = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=None, required=False)
        self.fields['parent'] = forms.IntegerField(widget=forms.HiddenInput, required=False)
