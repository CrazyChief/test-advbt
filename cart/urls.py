from django.conf.urls import include, url
from cart import views


# app_name = 'cart'
urlpatterns = [
    url('',  include('easycart.urls')),
    url('^$', views.CartDetail.as_view(), name='detail'),
]











