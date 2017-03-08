import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    """
    Category model
    """
    title = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField()

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

    def get_absolute_url(self):
        return reverse('products:ProductListByCategory', args=[self.title])


class Product(models.Model):
    """
    Product body
    """
    title = models.CharField(max_length=100)
    description = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField()
    status = models.BooleanField()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title

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
    #     return reverse('products:ProductDetail', args=[self.id])


class ProductVariation(models.Model):
    """
    Variations of every product.
    """
    title = models.CharField(max_length=150)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor_code = models.CharField(max_length=20, unique=True)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    quantity = models.IntegerField()
    rate = models.FloatField()
    is_new = models.BooleanField()
    is_available = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()

    class Meta:
        verbose_name = "Product variation"
        verbose_name_plural = "Products variations"

    def __str__(self):
        return str(self.product) + " - " + str(self.vendor_code)

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
    product = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    image = models.FileField(upload_to=upload_path)
    description = models.CharField(null=True, max_length=200)
    is_main = models.BooleanField()
    main_product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Product image"
        verbose_name_plural = "Products images"

    def __str__(self):
        return str(self.product)

    # def get_absolute_url(self):
    #     return reverse('products:ProductDetail', args=[self.product, self.image])


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


class Order(models.Model):
    """
    Order model. Stores detail information of every order
    """
    billing_first_name = models.CharField(max_length=100)
    billing_last_name = models.CharField(max_length=100)
    shipping_first_name = models.CharField(max_length=100)
    shipping_last_name = models.CharField(max_length=100)
    shipping_type = models.CharField(max_length=50)
    shipping_street = models.CharField(max_length=200, null=True)
    shipping_state = models.CharField(max_length=100, null=True)
    shipping_postcode = models.CharField(max_length=15, null=True)
    shipping_country = models.CharField(max_length=50, null=True)
    shipping_city = models.CharField(max_length=100, null=True)
    shipping_departament = models.CharField(max_length=400, null=True)
    shipping_to_home = models.BooleanField()
    shipping_phone = models.CharField(max_length=20)
    shipping_email = models.EmailField(max_length=254)

    shipping_total = models.FloatField()
    discount_code = models.CharField(max_length=20, null=True)
    total = models.FloatField()
    item_total = models.IntegerField()
    pay_status = models.BooleanField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ["-id"]

    def billing_name(self):
        return "%s %s" % (self.billing_first_name, self.billing_last_name)

    def __str__(self):
        return "%s %s %s" % (self.id, self.billing_name(), self.time)


class OrderItem(models.Model):
    """
    Order item model. Stores an information about every product in order
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_variation = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = "Order item"
        verbose_name_plural = "Order items"


class Discount(models.Model):
    """
    Discount model. Stores an information about discount in details
    """
    discount_title = models.CharField(max_length=200)
    discount_range = models.IntegerField()
    discount_code = models.CharField(max_length=20)
    discount_type = models.CharField(max_length=100)
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


