from django.shortcuts import get_object_or_404
from django.views import generic
from django.http import Http404, HttpResponsePermanentRedirect

from .models import Category, Product, ProductVariation, ProductImage, ProductReview


# def product_list(request, category_title=None):
#     category = None
#     categories = Category.objects.all()
#     # products = Product.objects.filter(is_available=True)
#     products = Product.objects.all()
#     prod_variations = ProductVariation.objects.all()
#     prod_images = ProductImage.objects.all()
#     if category_title:
#         category = get_object_or_404(Category, title=category_title)
#         products = products.filter(category=category)
#     return render(request, 'products/list.html', {
#         'category': category,
#         'categories': categories,
#         'products': products,
#         'prod_variations': prod_variations,
#         'prod_images': prod_images,
#     })
#
#
# def ProductDetail(request, id, vendor_code):
#     product = get_object_or_404((Product, ProductVariation, ProductImage), id=id, vendor_code=vendor_code)
#     return render(request, 'products/detail.html', {'product': product})


class IndexView(generic.ListView):
    template_name = 'products/list.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['products_list'] = Product.objects.all()
        context['product_variation_list'] = ProductVariation.objects.all()
        context['product_image_list'] = ProductImage.objects.all()
        return context

    # def get_search_hangler(self):
    #     pass


class ProductCategoryView(generic.TemplateView):
    # model = Category

    template_name = 'products/products_by_category.html'
    # queryset = Category.objects.all()
    context_object_name = 'category'

    def get(self, request, *args, **kwargs):
        self.category = self.get_category()

        return super(ProductCategoryView, self).get(request, *args, **kwargs)

    def get_category(self):
        if 'pk' in self.kwargs:
            return get_object_or_404(Category, pk=self.kwargs['pk'])
        raise Http404

    # def get_categories(self):
    #     return self.category.get_deferred_fields()

    # def get_queryset(self):
    #     return Category.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.category
        context['category_list'] = Category.objects.all()
        context['products_list'] = ProductVariation.objects.filter(product__category__pk=self.category.id)
        context['product_image_list'] = ProductImage.objects.filter(product__product__category__id=self.category.id)
        return context


class ProductView(generic.DetailView):
    model = ProductVariation
    template_name = 'products/detail.html'

    def get(self, request, *args, **kwargs):
        # self.category = self.get_category()
        # self.variations = self.get_variation_list()

        return super(ProductView, self).get(request, *args, **kwargs)

    # def get_category(self):
    #     if 'fk' in self.kwargs:
    #         return get_object_or_404(Category, pk=self.kwargs['fk'])
    #     raise Http404

    # def get_variation_list(self):
    #     if 'pk' in self.kwargs:
    #         main_product = ProductVariation.objects.filter(pk=self.kwargs['pk'])
    #         self.main_product = main_product.get()
    #         return get_object_or_404(ProductVariation.objects.filter(product=self.main_product.pk))
    #     raise Http404

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.filter(pk=self.kwargs['fk'])
        context['product_images'] = ProductImage.objects.filter(product=self.kwargs['pk'])
        context['product_reviews'] = ProductReview.objects.filter(product=self.kwargs['pk'])
        # context['product_variation_list'] = Product.objects.filter(productvariation=self.kwargs['pk'])
        # context['product_variation_list'] = self.variations
        return context






















