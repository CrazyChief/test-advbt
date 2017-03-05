from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Category, Product, ProductVariation, ProductImage, ProductReview


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True)
    if category_slug:
        category = get_object_or_404(Category, title=category_slug)
        products = products.filter(category=category)
    return render(request, 'products/index.html', {
        'category': category,
        'categories': categories,
        'products': products,
    })


# class IndexView(generic.ListView):
#     template_name = 'products/index.html'
#     context_object_name = 'categories'
#     # model = [Category, Product, ProductVariation, ProductImage]
#     queryset = Category.objects.order_by('-id')

    # def get_queryset(self):
    #     """Return all categories and products"""
    #     return Category.objects.order_by('-id')


# def index(request):
#     categories = Category.objects.order_by('-id')
#     output = ', '.join([cat.title for cat in categories])
#     return HttpResponse(output)
#
#
# def detail(request, title, product_id, product_variation_sku, product_review_id):
#     # response = "You're looking at the result of product %s."
#     return HttpResponse("You're looking at the result of product %s - %s in %s category." %
#                         (product_id, product_variation_sku, title))
#
