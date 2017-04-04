from django.contrib import admin
from .models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

    list_display = (
        'shipping_first_name',
        'shipping_last_name',
        'pay_status',
        'total',
        'created',
    )
    list_filter = [
        'shipping_type',
        'pay_status',
        'total',
        'created',
    ]


admin.site.register(Order, OrderAdmin)