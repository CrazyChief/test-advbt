from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormMixin
from django.http import Http404, HttpResponseForbidden
from django.urls import reverse
from django.conf import settings
from django.core import mail

from django.contrib.auth.models import User
from .models import Category, SubCategory, Product, ProductVariation, ProductImage, ProductReview, ProductQuestion
from .forms import ReviewForm, QuestionForm
# from cart.forms import CartAddProductForm


class IndexView(ListView):
    template_name = 'products/list.html'
    context_object_name = 'category_list'
    paginate_by = 10

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # context['products_list'] = Product.objects.filter(status__exact=True)
        context['product_variation_list'] = ProductVariation.objects.filter(product__status__exact=True).filter(status__exact=True)
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
        context['sub_category_list'] = SubCategory.objects.filter(category__exact=self.category.id)
        context['products_list'] = ProductVariation.objects.filter(product__category__pk=self.category.id)
        context['product_image_list'] = ProductImage.objects.filter(product__product__category__id=self.category.id)
        return context


class ProductView(DetailView, FormMixin):
    model = ProductVariation
    template_name = 'products/detail.html'
    form_class = ReviewForm
    question_form_class = QuestionForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.initial = {
                'name': request.user.username,
                'email': request.user.email,
            }
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

    def get_question_form_class(self):
        return self.question_form_class

    def get_question_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_question_form_class()
        return form_class(**self.get_form_kwargs())

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.filter(pk=self.kwargs['fk'])
        # kwargs['sizes'] = {size: self.model.objects.get_or_create(rate=str(size))[0] for size in range(10, 40)}
        context['product_images'] = ProductImage.objects.filter(product=self.kwargs['pk'])
        context['product_reviews'] = ProductReview.objects.filter(product=self.kwargs['pk'])
        context['product_variation_list'] = ProductVariation.objects.filter(product=self.get_product())
        context['questions'] = ProductQuestion.objects.filter(product=self.kwargs['pk']).filter(parent=None)
        context['same_products'] = ProductVariation.objects.filter(product=self.get_product())[:4]
        context['form'] = self.get_form()
        if self.request.user.is_authenticated:
            context['user'] = User.objects.get(pk=self.request.user.id)
        else:
            context['user'] = None
        context['question_form'] = self.get_question_form(form_class=self.question_form_class)
        return context

    def post(self, request, *args, **kwargs):
        if not request:
            return HttpResponseForbidden()
        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.get_form_class()
            form_name = 'form'
        else:
            form_class = self.get_question_form_class()
            form_name = 'question_form'
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(**{form_name: form})

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.product = ProductVariation.objects.get(pk=self.kwargs['pk'])
        if 'question_form' in self.request.POST:
            obj.parent = None
            try:
                parent_id = int(self.request.POST.get('parent'))
            except:
                parent_id = None

            if parent_id:
                parent_qs = ProductQuestion.objects.filter(pk=parent_id)
                if parent_qs.exists():
                    obj.parent = parent_qs.first()
                    # link = "http://127.0.0.1:8000" + self.get_success_url() + "#reply" + str(parent_id)
                    link = self.request.META['HTTP_REFERER'] + "#reply" + str(parent_id)
                    msg = "This user (%s) replied to your question. Follow this link: %s" % (obj.name, link)
                    with mail.get_connection() as connection:
                        mail.EmailMessage(
                            "Reply to question", msg, settings.DEFAULT_FROM_EMAIL, [parent_qs.get().email],
                            connection=connection
                        ).send()

            if self.request.user.is_authenticated:
                obj.user = User.objects.get(pk=self.request.user.id)
        obj.save()
        return super(ProductView, self).form_valid(form)

    def get_success_url(self):
        return reverse('products:detail', kwargs={'fk': self.kwargs['fk'], 'pk': self.kwargs['pk']})





















