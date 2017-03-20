from modeltranslation.translator import translator, TranslationOptions
from contacts.models import Phone


class PhoneTranslationOptions(TranslationOptions):
    fields = ('country_prefix',)


translator.register(Phone, PhoneTranslationOptions)
