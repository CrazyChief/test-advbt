from django.shortcuts import get_object_or_404
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import FormMixin
from django.http import Http404, HttpResponseForbidden, JsonResponse
from django.urls import reverse
from django.conf import settings
from django.db.models import Q
from django.contrib.auth.models import User

from .models import Category, SubCategory, Product, ProductVariation, ProductImage, ProductReview, ProductQuestion
from .forms import ReviewForm, QuestionForm
from .products import ProductBase

from meta.views import MetadataMixin
from templated_email import send_templated_mail

session_key = getattr(settings, 'PRODUCT_SESSION_KEY', 'products')


class Price(View):

    action = None
    required_params = ()

    def post(self, request):
        params = {}
        for param in self.required_params:
            try:
                params[param] = request.POST[param]
            except KeyError:
                return JsonResponse({
                    'error': 'MissingRequestParam',
                    'param': param,
                })
        product = Pr(request)
        action = getattr(product, self.action)
        try:
            action(**params)
        except KeyError:
            return JsonResponse({
                'error': 'MissingRequestParam',
            })
        return product.encode()


class SetPrice(Price):

    action = 'set_price_values'
    required_params = ('min_price', 'max_price',)


class ResetPrice(Price):

    action = 'reset'
    # required_params = ('min_price', 'max_price',)


class Pr(ProductBase):
    pass


class IndexView(ListView):
    template_name = 'products/list.html'
    context_object_name = 'products_list'
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        self.prod = ProductBase(request)
        return super(IndexView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return Product.objects.filter(Q(productvariation__price__gte=self.prod.get_price_values()['min_price']) &
                                      Q(productvariation__price__lte=self.prod.get_price_values()['max_price'])).\
            filter(status__exact=True).distinct()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['price_values'] = self.prod.get_price_values()
        return context


class ProductCategoryView(ListView):
    template_name = 'products/products_by_category.html'
    context_object_name = 'products_list'
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        self.category = self.get_category()
        self.prod = ProductBase(request)
        return super(ProductCategoryView, self).get(request, *args, **kwargs)

    def get_category(self):
        if 'pk' in self.kwargs:
            return get_object_or_404(Category, pk=self.kwargs['pk'])
        raise Http404

    def get_queryset(self):
        return Product.objects.filter(Q(productvariation__price__gte=self.prod.get_price_values()['min_price']) &
                                      Q(productvariation__price__lte=self.prod.get_price_values()['max_price'])).\
            filter(category__pk=self.category.id).filter(status__exact=True).distinct()

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.category
        context['category_list'] = Category.objects.filter(is_active__exact=True)
        context['sub_category_list'] = SubCategory.objects.filter(category__exact=self.category.id)
        context['price_values'] = self.prod.get_price_values()
        return context


class ProductSubCategoryView(ListView):
    template_name = 'products/products_by_subcategory.html'
    context_object_name = 'products_list'
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        self.prod = ProductBase(request)
        return super(ProductSubCategoryView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return Product.objects.filter(Q(productvariation__price__gte=self.prod.get_price_values()['min_price']) &
                                      Q(productvariation__price__lte=self.prod.get_price_values()['max_price'])).\
            filter(category__pk=self.kwargs['fk']).filter(sub_categories__slug__icontains=self.kwargs['slug']).\
            filter(status__exact=True).distinct()

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
        context['price_values'] = self.prod.get_price_values()
        return context


class ProductView(MetadataMixin, DetailView, FormMixin):
    model = Product
    template_name = 'products/detail.html'
    form_class = ReviewForm
    question_form_class = QuestionForm
    use_og = True

    def get(self, request, *args, **kwargs):
        self.title = self.get_product().title
        self.description = self.get_product().details
        self.image = "%s" % self.get_product().image
        self.url = self.get_success_url()
        self.object_type = 'Product'
        self.custom_namespace = 'product'
        if request.user.is_authenticated:
            self.initial = {
                'name': request.user.username,
                'email': request.user.email,
            }

        return super(ProductView, self).get(request, *args, **kwargs)

    def get_variation_list(self):
        if 'pk' in self.kwargs:
            return get_object_or_404(ProductVariation, product=self.get_product())

    def get_keywords(self):
        pass

    def get_product(self):
        if 'pk' in self.kwargs:
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
                    link = self.request.META['HTTP_REFERER'] + "#reply" + str(parent_id)
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
        elif 'form' in self.request.POST:
            send_templated_mail(
                template_name='review_noreply',
                from_email='noreply@sandbox8f86f5175eec47f39c7887ee6e45e3a9.mailgun.org',
                recipient_list=[obj.reviewer_email],
                context={
                    'full_name': obj.reviewer_name,
                    'product': obj.product.title,
                }
            )
        obj.save()
        return super(ProductView, self).form_valid(form)

    def get_success_url(self):
        return reverse('products:detail', kwargs={
            'fk': self.kwargs['fk'],
            'slug': self.kwargs['slug'],
            'pk': self.kwargs['pk']
        })
