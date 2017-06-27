from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormMixin, FormView
from django.http import Http404, HttpResponseForbidden
from django.urls import reverse
from django.conf import settings
from django.core import mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_filters.views import FilterView

from django.contrib.auth.models import User
from .filters import ProductFilter
from .models import Category, SubCategory, Product, ProductVariation, ProductImage, ProductReview, ProductQuestion
from .forms import ReviewForm, QuestionForm, FilterForm
# from cart.forms import CartAddProductForm


class IndexView(ListView):
    template_name = 'products/list.html'
    context_object_name = 'products_list'
    paginate_by = 20

    def get_queryset(self):
        return Product.objects.filter(status__exact=True)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        # context['product_variation_list'] = Product.objects.filter(status__exact=True)
        return context


class ProductCategoryView(ListView, FilterView):
    template_name = 'products/products_by_category.html'
    context_object_name = 'products_list'
    filterset_class = ProductFilter
    # form_class = FilterForm
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        self.category = self.get_category()

        # self.form_class = self.form_class(self.kwargs['pk'])
        return super(ProductCategoryView, self).get(request, *args, **kwargs)

    def get_category(self):
        if 'pk' in self.kwargs:
            return get_object_or_404(Category, pk=self.kwargs['pk'])
        raise Http404

    # def get_categories(self):
    #     return self.category.get_deferred_fields()

    def get_queryset(self):
        return Product.objects.filter(category__pk=self.category.id).filter(status__exact=True)

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.category
        context['category_list'] = Category.objects.filter(is_active__exact=True)
        context['sub_category_list'] = SubCategory.objects.filter(category__exact=self.category.id)
        # context['form'] = self.get_form()
        context['filter'] = self.filterset_class
        # print('Printed context from products_list: %s' % context)
        # context['products_list'] = Product.objects.filter(category__pk=self.category.id)
        return context


class ProductSubCategoryView(TemplateView):
    template_name = 'products/products_by_subcategory.html'

    def get(self, request, *args, **kwargs):
        return super(ProductSubCategoryView, self).get(request, *args, **kwargs)

    # def get_queryset(self):
    #     self.sub_category = get_object_or_404(SubCategory, self.args[0])
    #     return SubCategory.objects.filter(pk=self.sub_category)

    def get_sub_category(self):
        if 'slug' in self.kwargs:
            return get_object_or_404(SubCategory, slug=self.kwargs['slug'])
        raise Http404

    def get_context_data(self, **kwargs):
        context = super(ProductSubCategoryView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['fk'])
        context['category_list'] = Category.objects.filter(is_active__exact=True)
        context['sub_cat'] = self.get_sub_category()
        context['sub_category_list'] = SubCategory.objects.filter(category__exact=self.kwargs['fk'])
        # context['products_list'] = Product.objects.filter(sub_categories=self.get_sub_category())
        context['products_list'] = Product.objects.filter(category__pk=self.kwargs['fk']).filter(sub_categories__slug__icontains=self.kwargs['slug']).filter(status__exact=True)
        return context


class ProductView(DetailView, FormMixin):
    model = Product
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
            # self.prod_var = Product.objects.filter(pk=self.kwargs['pk'])
            return get_object_or_404(Product, pk=self.kwargs['pk'])
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
        context['category_list'] = Category.objects.filter(is_active__exact=True)
        # kwargs['sizes'] = {size: self.model.objects.get_or_create(rate=str(size))[0] for size in range(10, 40)}
        #
        # context['sub_category'] = SubCategory.objects.filter(pk=self.kwargs['id'])
        #
        context['product_images'] = ProductImage.objects.filter(product=self.kwargs['pk'])
        context['product_reviews'] = ProductReview.objects.filter(product=self.kwargs['pk'])
        context['product_variation_list'] = ProductVariation.objects.filter(product=self.get_product())
        context['questions'] = ProductQuestion.objects.filter(product=self.kwargs['pk']).filter(parent=None)
        context['same_products'] = Product.objects.filter(category_id=self.kwargs['fk']).filter(status__exact=True).exclude(pk=self.kwargs['pk'])[:4]
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
        obj.product = Product.objects.get(pk=self.kwargs['pk'])
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
        return reverse('products:detail', kwargs={'fk': self.kwargs['fk'], 'slug': self.kwargs['slug'], 'pk': self.kwargs['pk']})





















