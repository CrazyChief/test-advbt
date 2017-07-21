from django.db import models
from products.models import ProductVariation
from discounts.models import Discount


class Order(models.Model):
    """
    Order model. Stores detail information of every order
    """
    NEW_POST = 'N_P'
    ANOTHER_VARIANT = 'A_V'
    SHIPPING_TYPES = (
        (NEW_POST, 'New Post'),
        (ANOTHER_VARIANT, 'Another variant (We will call you back to clarify the details)'),
    )
    PAY_NOW = 'N'
    WHEN_RECEIVING = 'W_R'
    PAY_TYPES = (
        (PAY_NOW, 'Now'),
        (WHEN_RECEIVING, 'When receiving (for New Post only)'),
    )
    shipping_first_name = models.CharField(max_length=100)
    shipping_last_name = models.CharField(max_length=100)
    shipping_type = models.CharField(max_length=50, choices=SHIPPING_TYPES, default=ANOTHER_VARIANT)
    shipping_street = models.CharField(max_length=200, null=True, blank=True)
    shipping_home = models.CharField(max_length=20, null=True, blank=True)
    shipping_state = models.CharField(max_length=100, null=True, blank=True)
    shipping_postcode = models.CharField(max_length=15, null=True, blank=True)
    shipping_country = models.CharField(max_length=50, null=True, blank=True)
    shipping_city = models.CharField(max_length=100, null=True, blank=True)
    shipping_departament = models.CharField(max_length=400, null=True, blank=True)
    shipping_to_home = models.BooleanField(default=False)
    shipping_phone = models.CharField(max_length=20)
    shipping_email = models.EmailField(max_length=254)

    pay_type = models.CharField(max_length=40, choices=PAY_TYPES, default=PAY_NOW)
    # discount_code = models.ForeignKey(Discount, null=True, on_delete=models.SET_NULL)
    # total = models.FloatField(null=True, blank=True)
    # item_total = models.IntegerField()
    pay_status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def shipping_name(self):
        return "%s %s" % (self.shipping_first_name, self.shipping_last_name)

    def __str__(self):
        return "%s %s %s" % (self.id, self.shipping_name(), self.created)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.orderitem_set.all())


class OrderItem(models.Model):
    """
    Order item model. Stores an information about every product in order
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = "Order item"
        verbose_name_plural = "Order items"

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity












