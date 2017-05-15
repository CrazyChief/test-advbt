from django.views.generic import TemplateView
from products.models import Product
from bloggiz.models import Post


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all()[:3]
        context['posts'] = Post.objects.all()[:2]
        return context














