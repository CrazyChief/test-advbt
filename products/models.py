import datetime

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from colorfield.fields import ColorField


class Category(models.Model):
    """
    Category model
    """
    title = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def is_category_active(self):
        return self.is_active

    is_category_active.admin_order_field = 'is_active'
    is_category_active.boolean = True
    is_category_active.short_description = 'Is active?'


class SubCategory(models.Model):
    """
    Sub categories for products
    """
    PUBLISHED = True
    DRAFT = False
    STATUSES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
    )
    title = models.CharField(max_length=100, unique=True, verbose_name=_('Title'))
    category = models.ManyToManyField(Category, verbose_name=_("Category"))
    status = models.BooleanField(choices=STATUSES, default=DRAFT, verbose_name=_('Status'))

    class Meta:
        verbose_name = _("Sub Category")
        verbose_name_plural = _("Sub Categories")

    def __str__(self):
        return self.title

    def is_sub_category_active(self):
        return self.status

    is_sub_category_active.admin_order_field = 'status'
    is_sub_category_active.boolean = True
    is_sub_category_active.short_description = 'Is active?'


def upload_path(instance, filename):
    """
    Path to files
    :param instance:
    :param filename:
    :return:
    """
    return "products/{0}".format(filename)


class Product(models.Model):
    """
    Product body
    """
    PUBLISHED = True
    DRAFT = False
    STATUSES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
    )
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"))
    status = models.BooleanField(choices=STATUSES, default=DRAFT, verbose_name=_("Status"))
    price = models.FloatField(default=0, verbose_name=_("Price"))
    sku = models.CharField(max_length=20, unique=True, null=True)
    is_new = models.BooleanField(default=False, verbose_name=_("Is new"))
    is_available = models.BooleanField(default=False, verbose_name=_("Is available"))
    sub_categories = models.ManyToManyField(SubCategory, verbose_name=_("Sub categories"))
    image = models.FileField(upload_to=upload_path)
    date_added = models.DateTimeField(auto_now_add=True)
    details = RichTextField(verbose_name=_("Details"), blank=True)
    htu = RichTextField(verbose_name=_("How to use"), blank=True)
    composition = RichTextField(verbose_name=_("Composition"), blank=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + " - " + str(self.sku)

    def is_posted(self):
        return self.status

    is_posted.admin_order_field = 'status'
    is_posted.boolean = True
    is_posted.short_description = 'Is posted?'


class ProductVariation(models.Model):
    """
    Variations of every product.
    """
    PUBLISHED = True
    DRAFT = False
    STATUSES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    color_description = models.CharField(max_length=50, blank=True, verbose_name=_("Color description"))
    color_value = ColorField(default='#FF0000', verbose_name=_("Color value"))
    status = models.BooleanField(choices=STATUSES, default=DRAFT, verbose_name=_("Status"))

    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Product variation"
        verbose_name_plural = "Products variations"

    def get_main_image(self):
        return self.productimage_set.get(is_main=True).image

    def __str__(self):
        return str(self.product) + " - " + str(self.color_description)

    def is_posted(self):
        return self.status

    is_posted.admin_order_field = 'status'
    is_posted.boolean = True
    is_posted.short_description = 'Is posted?'


class ProductImage(models.Model):
    """
    Store of images for all products
    """
    product = models.ForeignKey(ProductVariation, null=True, on_delete=models.SET_NULL)
    image = models.FileField(upload_to=upload_path)
    description = models.CharField(null=True, max_length=200)
    is_main = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Product image"
        verbose_name_plural = "Products images"
        ordering = ["-is_main"]

    def __str__(self):
        return str(self.product)


class ProductReview(models.Model):
    """
    Reviews of every product
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    reviewer_name = models.CharField(max_length=100)
    reviewer_email = models.EmailField(max_length=254)
    review_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Product Review"
        verbose_name_plural = "Products Reviews"

    def __str__(self):
        return self.reviewer_name + " - " + self.reviewer_email

    def product_name(self):
        return self.product

    product_name.admin_order_field = 'product'
    product_name.short_description = 'Review for product'


class ProductQuestion(models.Model):
    """
    Questions for every product
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    question = models.TextField()
    name = models.CharField(max_length=240)
    email = models.CharField(max_length=240)
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name=_('Parent'))
    user = models.ForeignKey(User, null=True, blank=True, verbose_name=_('User'))
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]
        verbose_name = _("Product Question")
        verbose_name_plural = _("Product Questions")

    def __str__(self):
        return self.name + " - " + self.email

    def product_name(self):
        return self.product

    def children(self):     # replies
        return ProductQuestion.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

    product_name.admin_order_field = 'product'
    product_name.short_description = 'Question for product'


class Discount(models.Model):
    """
    Discount model. Stores an information about discount in details
    """
    PER_PRODUCT = 'P_P'
    FOR_ALL = 'F_A'
    TYPES = (
        (PER_PRODUCT, 'Per product'),
        (FOR_ALL, 'For all'),
    )
    discount_title = models.CharField(max_length=200)
    discount_range = models.IntegerField()
    discount_code = models.CharField(max_length=20)
    discount_type = models.CharField(max_length=20, choices=TYPES, default=FOR_ALL)
    discount_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    discount_start_period = models.DateTimeField()
    discount_end_period = models.DateTimeField()
    discount_description = models.TextField()

    class Meta:
        verbose_name = "Discount"
        verbose_name_plural = "Discounts"

    def __str__(self):
        return "%s %s" % (self.discount_code, self.discount_type)

    def out_of_date(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.discount_end_period <= now

    out_of_date.admin_order_field = 'discount_end_period'
    out_of_date.boolean = True
    out_of_date.short_description = 'Is out of date?'


