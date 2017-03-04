from django.contrib import admin
from django.db.models import TextField
from .models import Category, Product, ProductVariation, ProductImage, ProductReview, Order, OrderItem, Discount
from ckeditor.widgets import CKEditorWidget


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_category_active',
    )
    list_filter = [
        'title',
        'is_active',
    ]


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductVariationInline(admin.TabularInline):
    model = ProductVariation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariationInline, ProductImageInline]

    list_display = (
        'title',
        'date_added',
        'is_product_available',
        'is_posted',
    )
    list_filter = [
        'title',
        'date_added',
        'is_available',
        'status',
    ]
    formfield_overrides = {TextField: {'widget': CKEditorWidget}}


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'reviewer_name',
        'reviewer_email',
        'review_added',
    )
    list_filter = [
        'reviewer_name',
        'reviewer_email',
        'review_added',
    ]
    formfield_overrides = {TextField: {'widget': CKEditorWidget}}


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

    list_display = (
        'billing_name',
        'pay_status',
        'total',
        'time',
    )
    list_filter = [
        'billing_first_name',
        'billing_last_name',
        'pay_status',
        'total',
        'time',
    ]


class DiscountAdmin(admin.ModelAdmin):
    list_display = (
        'discount_title',
        'discount_range',
        'discount_code',
        'out_of_date',
    )
    list_filter = [
        'discount_title',
        'discount_range',
        'discount_code',
        'discount_start_period',
        'discount_end_period',
    ]
    formfield_overrides = {TextField: {'widget': CKEditorWidget}}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Discount, DiscountAdmin)

