from django.conf.urls import url
from . import views


app_name = "orders"
urlpatterns = [
    url('^$', views.CheckoutView.as_view(), name='checkout'),
]

