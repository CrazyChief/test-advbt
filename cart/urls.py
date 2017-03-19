from django.conf.urls import url
from . import views


appname = 'cart'
urlpatterns = [
    url(r'^$', views.CartDetail.as_view(), name='detail'),
    url(r'^remove/(?P<product_id>\d+)/', views.CartDelete.as_view(), name='delete'),
    url(r'^add/(?P<product_id>\d+)/', views.CartAdd.as_view(), name='add'),
]











