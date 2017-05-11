import datetime

from django.db import models
from django.utils import timezone
# from django.urls import reverse
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
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(choices=STATUSES, default=DRAFT)
    details = RichTextField(verbose_name=_("Details"), blank=True)
    htu = RichTextField(verbose_name=_("How to use"), blank=True)
    composition = RichTextField(verbose_name=_("Composition"), blank=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title

    def is_posted(self):
        return self.status

    is_posted.admin_order_field = 'status'
    is_posted.boolean = True
    is_posted.short_description = 'Is posted?'

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'pk': self.pk})


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
    title = models.CharField(max_length=150)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku = models.CharField(max_length=20, unique=True, null=True)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    color_description = models.CharField(max_length=50, blank=True)
    color_value = ColorField(default='#FF0000')
    is_new = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)
    status = models.BooleanField(choices=STATUSES, default=DRAFT)
    date_added = models.DateTimeField(auto_now_add=True)
    # description = RichTextField()

    class Meta:
        verbose_name = "Product variation"
        verbose_name_plural = "Products variations"

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'pk': self.pk})

    def get_main_image(self):
        return self.productimage_set.get(is_main=True).image

    def update_quantity(self, ordered_quantity):
        self.quantity -= ordered_quantity
        if self.quantity == 0:
            self.is_available = False
        return self.save()

    def __str__(self):
        return str(self.product) + " - " + str(self.sku)

    def is_product_available(self):
        return self.is_available

    def is_posted(self):
        return self.status

    is_product_available.admin_order_field = 'is_available'
    is_product_available.boolean = True
    is_product_available.short_description = 'Is available?'

    is_posted.admin_order_field = 'status'
    is_posted.boolean = True
    is_posted.short_description = 'Is posted?'

    # def get_absolute_url(self):
    #     return reverse('products:ProductDetail', args=[self.product, self.vendor_code])


def upload_path(instance, filename):
    """
    Path to files
    :param instance:
    :param filename:
    :return:
    """
    return "products/{0}".format(filename)


class ProductImage(models.Model):
    """
    Store of images for all products
    """
    product = models.ForeignKey(ProductVariation, null=True, on_delete=models.SET_NULL)
    image = models.FileField(upload_to=upload_path)
    description = models.CharField(null=True, max_length=200)
    is_main = models.BooleanField(default=False)
    # main_product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

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
    product = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
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
    product = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
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
    discount_product = models.ForeignKey(ProductVariation, on_delete=models.CASCADE, null=True)
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


