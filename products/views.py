from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormMixin
from django.http import Http404, HttpResponseForbidden
from django.urls import reverse

from .models import Category, Product, ProductVariation, ProductImage, ProductReview, ProductAnswer
from .forms import ReviewForm
from cart.forms import CartAddProductForm


class IndexView(ListView):
    template_name = 'products/list.html'
    context_object_name = 'category_list'
    paginate_by = 10

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['products_list'] = Product.objects.all()
        context['product_variation_list'] = ProductVariation.objects.all()
        context['product_image_list'] = ProductImage.objects.all()
        return context


class ProductCategoryView(TemplateView):
    # model = Category

    template_name = 'products/products_by_category.html'
    # queryset = Category.objects.all()
    context_object_name = 'category'
    paginate_by = 20

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


class ProductView(DetailView, FormMixin):
    model = ProductVariation
    template_name = 'products/detail.html'
    form_class = ReviewForm
    # answer_form_class = CartAddProductForm

    def get(self, request, *args, **kwargs):
        # self.category = self.get_category()
        # self.variations = self.get_variation_list()

        return super(ProductView, self).get(request, *args, **kwargs)

    def get_variation_list(self):
        if 'pk' in self.kwargs:
            return get_object_or_404(ProductVariation, product=self.get_product())

    def get_product(self):
        if 'pk' in self.kwargs:
            self.prod_var = ProductVariation.objects.filter(pk=self.kwargs['pk'])
            return get_object_or_404(Product, pk=self.prod_var.get().product.pk)
        raise Http404

    # def get_answer_form_class(self):
    #     return self.answer_form_class
    #
    # def get_answer_form(self, form_class=None):
    #     if form_class is None:
    #         form_class = self.get_answer_form_class()
    #     return form_class(**self.get_form_kwargs())

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.filter(pk=self.kwargs['fk'])
        # kwargs['sizes'] = {size: self.model.objects.get_or_create(rate=str(size))[0] for size in range(10, 40)}
        context['product_images'] = ProductImage.objects.filter(product=self.kwargs['pk'])
        context['product_reviews'] = ProductReview.objects.filter(product=self.kwargs['pk'])
        context['product_variation_list'] = ProductVariation.objects.filter(product=self.get_product())
        context['answers'] = ProductAnswer.objects.filter(product=self.kwargs['pk'])
        context['same_products'] = ProductVariation.objects.filter(product=self.get_product())[:4]
        context['form'] = self.get_form()
        # context['answer_form'] = self.get_answer_form(form_class=self.answer_form_class)
        return context

    def post(self, request, *args, **kwargs):
        if not request:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.product = ProductVariation.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return super(ProductView, self).form_valid(form)

    def get_success_url(self):
        return reverse('products:detail', kwargs={'fk': self.kwargs['fk'], 'pk': self.kwargs['pk']})





















