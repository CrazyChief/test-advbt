from django.contrib import admin
from .models import Cy


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'dimension', 'is_active')
    list_filter = ['active', 'name',]


admin.site.register(Cy, CurrencyAdmin)
