from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin, TranslationTabularInline
from .models import Post, Tag
from django.db.models import TextField, FileField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdmin(TabbedTranslationAdmin):
    prepopulated_fields = {"slug": ("title",)}
    radio_fields = {'is_published': admin.HORIZONTAL}
    list_display = (
        'title',
        'is_post_published',
        'date_added',
    )
    list_filter = [
        'date_added',
        'is_published',
    ]
    formfield_overrides = {
        TextField: {'widget': CKEditorUploadingWidget},
    }


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
