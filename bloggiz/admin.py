from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin, TranslationTabularInline
from .models import Post, Tag
from django.db.models import TextField
from ckeditor.widgets import CKEditorWidget


class PostAdmin(TabbedTranslationAdmin):
    list_display = (
        'title',
        'is_post_published',
        'date_added',
    )
    list_filter = [
        'date_added',
        'is_published',
    ]
    formfield_overrides = {TextField: {'widget': CKEditorWidget}}


class TagAdmin(TabbedTranslationAdmin):
    list_display = (
        'title',
        'is_active',
        'date_added',
    )
    list_filter = [
        'title',
        'is_active',
        'date_added',
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
