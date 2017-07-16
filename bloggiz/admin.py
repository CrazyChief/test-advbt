from django.contrib import admin
# from imagekit.admin import AdminThumbnail
# from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin, TranslationTabularInline
from .models import Post, Comments
from django.db.models import TextField, FileField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from image_cropping import ImageCroppingMixin


# class PostAdmin(TabbedTranslationAdmin):
class PostAdmin(ImageCroppingMixin, admin.ModelAdmin):
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


# class TagAdmin(TabbedTranslationAdmin):
#     list_display = (
#         'title',
#         'is_active',
#         'date_added',
#     )
#     list_filter = [
#         'title',
#         'is_active',
#         'date_added',
#     ]


class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'date_added',
    )
    list_filter = ['date_added']
    formfield_overrides = {
        TextField: {'widget': CKEditorUploadingWidget},
    }


admin.site.register(Post, PostAdmin)
# admin.site.register(Tag, TagAdmin)
admin.site.register(Comments, CommentsAdmin)
