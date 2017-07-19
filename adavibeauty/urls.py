"""adavibeauty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

# urlpatterns = i18n_patterns(
#     url(r'^$', views.IndexView.as_view()),
#     url(r'^i18n/', include('django.conf.urls.i18n')),
#     url(r'^cart/', include('cart.urls', namespace='cart')),
#     url(r'^checkout/', include('orders.urls', namespace='orders')),
#     url(r'^ckeditor/', include('ckeditor_uploader.urls')),
#     url(r'^contacts/', include('contacts.urls', namespace='contacts')),
#     url(r'^cy/', include('cy.urls', namespace='cy')),
#     url(r'^products/', include('products.urls', namespace='products')),
#     url(r'^blog/', include('bloggiz.urls', namespace='bloggiz')),
#     url(r'^subscribers/', include('subscribers.urls', namespace='subscribers')),
#     url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
#     url(r'^admin/', admin.site.urls),
# )
urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^checkout/', include('orders.urls', namespace='orders')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^contacts/', include('contacts.urls', namespace='contacts')),
    url(r'^cy/', include('cy.urls', namespace='cy')),
    url(r'^products/', include('products.urls', namespace='products')),
    url(r'^blog/', include('bloggiz.urls', namespace='bloggiz')),
    url(r'^subscribers/', include('subscribers.urls', namespace='subscribers')),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^payment/', include('payment.urls', namespace='payment')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)











