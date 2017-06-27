from django.conf.urls import url

from . import views



app_name = 'products'
# urlpatterns = [
#     # ex: /products/all/
#     url(r'^$', views.product_list, name='product_list'),
#     url(r'^(?P<category_title>[-\w]+)/$', views.product_list, name='ProductListByCategory'),
#     url(r'^(?P<id>\d+)/(?P<vendor_code>[0-9]+)/$', views.ProductDetail, name='ProductDetail'),
#     # ex: /products/face/1/2101/
#     # url(r'^(?P<title>[a-z]+)/(?P<product_id>[0-9]+)/(?P<product_variation_sku>[0-9]+)/$', views.detail, name='detail'),
#
# ]

urlpatterns = [
    # ex: /products/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /products/1/
    url(r'^(?P<pk>[0-9]+)/$', views.ProductCategoryView.as_view(), name='products_by_category'),
    # ex: /products/1/qwerty/
    url(r'^(?P<fk>[0-9]+)/(?P<slug>[-\w]+)/$', views.ProductSubCategoryView.as_view(), name='products_by_subcategory'),
    # ex: /products/1/qwerty/1/
    url(r'^(?P<fk>[0-9]+)/(?P<slug>[-\w]+)/(?P<pk>[0-9]+)/$', views.ProductView.as_view(), name='detail'),
    # url(r'^(?P<fk>[0-9]+)/(?P<pk>[0-9]+)/$', views.ProductView.as_view(), name='detail'),

    # url(r'^(?P<fk>[0-9]+)/(?P<pk>[0-9]+)/$', views.ProductReviewCreate.as_view(), name='review-add'),
]