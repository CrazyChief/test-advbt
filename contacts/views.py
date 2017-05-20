from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy as _
from .models import Review, Location, Email, Phone
from .forms import ReviewForm
from products.models import Category


class ReviewCreate(CreateView):
    template_name = 'contacts/index.html'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super(ReviewCreate, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.filter(is_active=True)
        context['locations'] = Location.objects.all()
        context['emails'] = Email.objects.all()
        context['phones'] = Phone.objects.all()
        return context

    def get_success_url(self):
        return _('contacts:index')

