from django.contrib import admin
from django.db.models import TextField
# from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin, TranslationTabularInline
from .models import Category, SubCategory, Product, ProductVariation, ProductImage, ProductReview, ProductQuestion
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# class CategoryAdmin(TabbedTranslationAdmin):
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_category_active',
    )
    list_filter = [
        'title',
        'is_active',
    ]


# class SubCategoryAdmin(TabbedTranslationAdmin):
class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'title',
        'is_sub_category_active',
    )
    list_filter = [
        'title',
        'status',
    ]
    filter_horizontal = ('category',)


# class ProductImageInline(TranslationTabularInline):
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


# class ProductAdmin(TabbedTranslationAdmin):
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date_added',
        'is_posted',
    )
    list_filter = [
        'date_added',
        'status',
    ]
    formfield_overrides = {TextField: {'widget': CKEditorUploadingWidget}}
    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'status', 'is_new', 'is_available', 'sub_categories',),
        }),
        ('Image', {
            'fields': ('image',),
        }),
        ('Description', {
            'classes': ('collapse',),
            'fields': ('details', 'htu', 'composition'),
        }),
    )
    # inlines = [KeywordAdmin]
    # filter_horizontal = ('keywords',)


# class ProduvtVariationAdmin(TabbedTranslationAdmin):
class ProductVariationAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

    list_display = (
        'product',
        'is_posted',
    )
    list_filter = [
        'date_added',
        'status',
    ]


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
    formfield_overrides = {TextField: {'widget': CKEditorUploadingWidget}}


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
    formfield_overrides = {TextField: {'widget': CKEditorUploadingWidget}}


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariation, ProductVariationAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(ProductQuestion, ProductQuestionAdmin)
