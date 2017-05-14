from django.contrib import admin
from django.db.models import TextField
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin, TranslationTabularInline
from .models import Category, SubCategory, Product, ProductVariation, ProductImage, ProductReview, ProductQuestion, Discount
from ckeditor.widgets import CKEditorWidget


class CategoryAdmin(TabbedTranslationAdmin):
    list_display = (
        'title',
        'is_category_active',
    )
    list_filter = [
        'title',
        'is_active',
    ]


class SubCategoryAdmin(TabbedTranslationAdmin):
    list_display = (
        'title',
        'is_sub_category_active',
    )
    list_filter = [
        'title',
        'status',
    ]
    filter_horizontal = ('category',)


class ProductImageInline(TranslationTabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(TabbedTranslationAdmin):
    list_display = (
        'title',
        'date_added',
        'is_posted',
    )
    list_filter = [
        'title',
        'date_added',
        'status',
    ]


class ProduvtVariationAdmin(TabbedTranslationAdmin):
    inlines = [ProductImageInline]

    list_display = (
        'title',
        'sku',
        'is_product_available',
        'is_posted',
    )
    list_filter = [
        'title',
        'sku',
        'date_added',
        'is_available',
        'status',
    ]
    formfield_overrides = {TextField: {'widget': CKEditorWidget}}
    filter_horizontal = ('sub_categories',)


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


class ProductQuestionAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'name',
        'email',
        'date_added',
    )
    list_filter = [
        'date_added',
    ]
    formfield_overrides = {TextField: {'widget': CKEditorWidget}}


class DiscountAdmin(TabbedTranslationAdmin):
    list_display = (
        'discount_title',
        'discount_type',
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
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariation, ProduvtVariationAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(ProductQuestion, ProductQuestionAdmin)
admin.site.register(Discount, DiscountAdmin)

