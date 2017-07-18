from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.http import Http404, HttpResponseForbidden
from django.urls import reverse
from django.conf import settings
from django.core import mail

from .models import Post, Comments
from .forms import CommentForm
from products.models import Category
from meta.views import MetadataMixin, Meta
from templated_email import send_templated_mail


class IndexView(ListView):
    model = Post
    template_name = "bloggiz/list.html"
    context_object_name = 'post_list'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.filter(is_active=True)
        return context


class PostView(MetadataMixin, DetailView, FormMixin):
    model = Post
    template_name = "bloggiz/detail.html"
    form_class = CommentForm
    use_og = True

    def get(self, request, *args, **kwargs):
        self.title = self.get_post().title
        self.description = self.get_post().content
        self.image = "%s" % self.get_post().cover_picture
        self.url = self.get_success_url()
        self.object_type = 'Article'
        self.custom_namespace = 'blog'
        if request.user.is_authenticated:
            self.initial = {
                'name': request.user.username,
                'email': request.user.email,
            }
        # print(request.META['HTTP_REFERER'])
        return super(PostView, self).get(request, *args, **kwargs)

    def get_post(self):
        if 'slug' in self.kwargs:
            # self.prod_var = Product.objects.filter(pk=self.kwargs['pk'])
            return get_object_or_404(Post, slug=self.kwargs['slug'])
        raise Http404

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['single_post'] = Post.objects.get(slug=self.kwargs['slug'])
        context['comments'] = Comments.objects.filter(post__slug=self.kwargs['slug']).filter(parent=None)
        context['category_list'] = Category.objects.filter(is_active=True)
        context['form'] = self.get_form()
        if self.request.user.is_authenticated:
            context['user'] = User.objects.get(pk=self.request.user.id)
        else:
            context['user'] = None

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
        obj.parent = None
        try:
            parent_id = int(self.request.POST.get('parent'))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comments.objects.filter(pk=parent_id)
            if parent_qs.exists():
                obj.parent = parent_qs.first()
                # link = "http://127.0.0.1:8000" + self.get_success_url() + "#reply" + str(parent_id)
                link = self.request.META['HTTP_REFERER'] + "#reply" + str(parent_id)
                # msg = "This user (%s) replied to your comment. Follow this link: %s" % (obj.name, link)
                # with mail.get_connection() as connection:
                #     mail.EmailMessage(
                #         "Reply to comment", msg, settings.DEFAULT_FROM_EMAIL, [parent_qs.get().email],
                #         connection=connection
                #     ).send()
                send_templated_mail(
                    template_name='comment_reply',
                    from_email='noreply@sandbox8f86f5175eec47f39c7887ee6e45e3a9.mailgun.org',
                    recipient_list=[parent_qs.get().email],
                    context={
                        'full_name': parent_qs.get().name,
                        'user': obj.name,
                        'link': link
                    }
                )

        if self.request.user.is_authenticated:
            obj.user = User.objects.get(pk=self.request.user.id)
        obj.save()
        return super(PostView, self).form_valid(form)

    def get_success_url(self):
        return reverse('bloggiz:detail', kwargs={'slug': self.kwargs['slug']})
