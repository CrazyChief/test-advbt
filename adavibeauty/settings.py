"""
Django settings for adavibeauty project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import PIL

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't0fd&$z^=g5kwn%^obiwpcrzs%o3!s@b3@$413%4ye@nib97bm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    # 'crazychief.pythonanywhere.com',
    'd17cfc19.ngrok.io',
    # '127.0.0.1',
    ]


# Application definition

INSTALLED_APPS = [
    # 'modeltranslation',
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products.apps.ProductsConfig',
    'cart.apps.CartConfig',
    'discounts.apps.DiscountsConfig',
    'orders.apps.OrdersConfig',
    'contacts.apps.ContactsConfig',
    'bloggiz.apps.BloggizConfig',
    'cy.apps.CyConfig',
    'subscribers.apps.SubscribersConfig',
    'ckeditor',
    'ckeditor_uploader',
    'colorfield',
    'star_ratings',
    'easycart',
    'django_social_share',
    'analytical',
    'sekizai',
    'meta',
    'easy_thumbnails',
    'image_cropping',
    'anymail',
    'paypal.standard.ipn',
    'payment.apps.PaymentConfig',
    # 'django_filters',
    # 'django_select2',
]

from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'adavibeauty.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
            # '/home/CrazyChief/test-advbt/templates/',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cy.context_processors.currency',
                'easycart.context_processors.cart',
                'products.context_processors.product',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

WSGI_APPLICATION = 'adavibeauty.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# Connection parameters for localhost
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'adavibeauty',
        'USER': 'postgres',
        'PASSWORD': 'NumberOne123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# Connection parameters for hosting
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'adavibeauty',
#         'USER': 'crazycat',
#         'PASSWORD': 'NumberOne123',
#         'HOST': 'CrazyChief-434.postgres.pythonanywhere-services.com',
#         'PORT': '10434',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                # your extra plugins here
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                # 'devtools',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath'
            ]),
    },
    # 'comment': {
    #     # 'skin': 'moono',
    #     'toolbar_Basic': [
    #         ['Source', '-', 'Bold', 'Italic']
    #     ],
    #     'toolbar_YourCustomToolbarConfig': [
    #         {'name': 'basicstyles',
    #          'items': ['Bold', 'Italic', 'Underline', 'Strike', '-']},
    #         {'name': 'paragraph',
    #          'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft',
    #              'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', ]},
    #         {'name': 'styles', 'items': ['Styles', 'Font', 'FontSize']},
    #         {'name': 'colors', 'items': ['TextColor', 'BGColor']},
    #         {'name': 'about', 'items': ['About']},
    #     ],
    #     'toolbar': 'YourCustomToolbarConfig',
    #     'tabSpaces': 2,
    #     'extraPlugins': ','.join(
    #         [
    #             # your extra plugins here
    #             'div',
    #             'autolink',
    #             'autoembed',
    #             'embedsemantic',
    #             'autogrow',
    #             # 'devtools',
    #             'widget',
    #             'lineutils',
    #             # 'clipboard',
    #             'dialog',
    #             'dialogui',
    #             'elementspath'
    #         ]),
    # }
}

# Email

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_USE_SSL = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 465
# EMAIL_HOST_USER = 'danilovdmitry94@gmail.com'
# EMAIL_HOST_PASSWORD = '609NumberOne$$123'
# DEFAULT_FROM_EMAIL = 'danilovdmitry94@gmail.com'
# # DEFAULT_TO_EMAIL = 'to email'

EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'danilovdmitry94@gmail.com'
EMAIL_HOST_PASSWORD = '609NumberOne$$123'
DEFAULT_FROM_EMAIL = 'danilovdmitry94@gmail.com'
# DEFAULT_TO_EMAIL = 'to email'


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

# MODELTRANSLATION_DEFAULT_LANGUAGE = 'en-us'
LANGUAGE_CODE = 'en-us'
#
# LANGUAGES = (
#     ('en-us', 'English'),
#     ('ru', 'Russian'),
#     ('uk', 'Ukrainian'),
# )

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True

LOCALE_PATHS = (
    'locale',
    # os.path.join(BASE_DIR, 'locale'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    '/static/',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CKEDITOR_IMAGE_BACKEND = PIL
CKEDITOR_UPLOAD_PATH = "ckeditor/uploads/"

EASYCART_CART_CLASS = 'cart.views.Cart'

CART_SESSION_ID = 'cart'

GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-102508308-1'

# PRODUCT_SESSION_ID = 'product'
PRODUCTS_PROD_CLASS = 'products.views.Prod'

STAR_RATINGS_RERATE = False
STAR_RATINGS_STAR_HEIGHT = 20
STAR_RATINGS_ANONYMOUS = True

META_SITE_PROTOCOL = 'http'
META_SITE_DOMAIN = 'd17cfc19.ngrok.io'
META_SITE_NAME = 'Adavibeauty'
META_USE_OG_PROPERTIES = True

IMAGE_CROPPING_BACKEND = 'image_cropping.backends.easy_thumbs.EasyThumbnailsBackend'
IMAGE_CROPPING_BACKEND_PARAMS = {}

ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": "key-7be344612b0888788a26c6de180f1d5a",
    "MAILGUN_SENDER_DOMAIN": 'crazychief.pythonanywhere.com',  # your Mailgun domain, if needed
}

TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django.TemplateBackend'

PAYPAL_RECEIVER_EMAIL = 'danilovdmitry94-bussines@gmail.com'
PAYPAL_TEST = True
