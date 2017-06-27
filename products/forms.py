from django import forms
from django.http.request import HttpRequest
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import ProductReview, ProductQuestion, Product, ProductVariation, Category, SubCategory


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


class FilterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        self.queryset = SubCategory.objects.all()
        self.fields['title'] = forms.ModelMultipleChoiceField(queryset=self.queryset, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = SubCategory
        fields = ['title']

















