from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Location, Email, Phone, Review


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'company_name',
        'location',
    )


class EmailAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'is_email_active',
    )


class PhoneAdmin(TabbedTranslationAdmin):
    list_display = (
        'country_prefix',
        'phone',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'status',
        'date_added',
    )


admin.site.register(Location, LocationAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Review, ReviewAdmin)
















