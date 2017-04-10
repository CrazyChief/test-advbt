from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.http import Http404, HttpResponseForbidden
from django.urls import reverse

from .models import Post, Comments
from .forms import CommentForm


class IndexView(ListView):
    model = Post
    template_name = "bloggiz/list.html"
    context_object_name = 'post_list'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.all()


class PostView(DetailView, FormMixin):
    model = Post
    template_name = "bloggiz/detail.html"
    form_class = CommentForm
    initial = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.initial = {
                # 'user': request.user,
                'name': request.user.username,
                'email': request.user.email,
            }
        return super(PostView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['single_post'] = Post.objects.get(slug=self.kwargs['slug'])
        context['comments'] = Comments.objects.filter(post__slug=self.kwargs['slug'])
        if not self.request.user.is_authenticated:
            context['user'] = None
        else:
            context['user'] = User.objects.get(pk=self.request.user.id)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request:
            return HttpResponseForbidden
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.post = Post.objects.get(slug=self.kwargs['slug'])
        if self.request.user.is_authenticated:
            obj.user = User.objects.get(pk=self.request.user.id)
        obj.save()
        return super(PostView, self).form_valid(form)

    def get_success_url(self):
        return reverse('bloggiz:detail', kwargs={'slug': self.kwargs['slug']})
