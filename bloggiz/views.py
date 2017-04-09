from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Tag


class IndexView(ListView):
    model = Post
    template_name = "bloggiz/list.html"
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.all()


class PostView(DetailView):
    model = Post
    template_name = "bloggiz/detail.html"

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['single_post'] = Post.objects.get(slug=self.kwargs['slug'])
        return context
