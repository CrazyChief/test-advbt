from modeltranslation.translator import translator, TranslationOptions
from products.models import Category, Product, ProductVariation, ProductImage, Discount


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'details', 'htu', 'composition',)


class ProductVariationTranslationOptions(TranslationOptions):
    fields = ('title', 'color_description',)


class ProductImageTranslationOptions(TranslationOptions):
    fields = ('description',)


class DiscountTranslationOptions(TranslationOptions):
    fields = ('discount_title', 'discount_description',)


translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(ProductVariation, ProductVariationTranslationOptions)
translator.register(ProductImage, ProductImageTranslationOptions)
translator.register(Discount, DiscountTranslationOptions)





