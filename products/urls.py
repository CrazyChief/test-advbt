from django.conf.urls import url

from . import views


app_name = 'products'

urlpatterns = [
    url(r'^set/$', views.SetPrice.as_view(), name='set-price'),
    url(r'^reset/$', views.ResetPrice.as_view(), name='reset-price'),
    # ex: /products/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /products/1/
    url(r'^(?P<pk>[0-9]+)/$', views.ProductCategoryView.as_view(), name='products_by_category'),
    # ex: /products/1/qwerty/
    url(r'^(?P<fk>[0-9]+)/(?P<slug>[-\w]+)/$', views.ProductSubCategoryView.as_view(), name='products_by_subcategory'),
    # ex: /products/1/qwerty/1/
    url(r'^(?P<fk>[0-9]+)/(?P<slug>[-\w]+)/(?P<pk>[0-9]+)/$', views.ProductView.as_view(), name='detail'),
]
