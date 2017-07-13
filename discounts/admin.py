from django.contrib import admin
from django.db.models import TextField
from .models import Discount
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# class DiscountAdmin(TabbedTranslationAdmin):
class DiscountAdmin(admin.ModelAdmin):
    list_display = (
        'discount_title',
        'discount_code',
        'discount_range',
        'out_of_date',
    )
    list_filter = [
        'discount_code',
        'discount_range',
        'discount_start_period',
        'discount_end_period',
    ]
    formfield_overrides = {TextField: {'widget': CKEditorUploadingWidget}}
    search_fields = ['discount_code',]


# admin.site.register(Discount, DiscountAdmin)
