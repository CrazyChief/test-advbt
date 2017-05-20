from django.views.generic import TemplateView
from products.models import Category, Product
from bloggiz.models import Post


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.filter(is_active=True)
        context['products'] = Product.objects.filter(is_new__exact=True)[:3]
        context['posts'] = Post.objects.all()[:2]
        return context














