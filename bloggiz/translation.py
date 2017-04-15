from modeltranslation.translator import translator, TranslationOptions
from .models import Post


# class CategoryTranslationOptions(TranslationOptions):
#     fields = ('',)


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'pretext', 'content')


# class TagTranslationOptions(TranslationOptions):
#     fields = ('title', 'description',)


# translator.register(Category, CategoryTranslationOptions)
translator.register(Post, PostTranslationOptions)
# translator.register(Tag, TagTranslationOptions)
