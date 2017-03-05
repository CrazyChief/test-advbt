from django.conf.urls import url

from . import views


urlpatterns = [
    # ex: /products/all/
    url(r'^$', views.product_list, name='product_list'),
    # ex: /products/face/1/2101/
    # url(r'^(?P<title>[a-z]+)/(?P<product_id>[0-9]+)/(?P<product_variation_sku>[0-9]+)/$', views.detail, name='detail'),

]