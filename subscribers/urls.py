from django.conf.urls import url
from . import views


app_name = 'subscribers'
urlpatterns = [
    url(r'^add/$', views.SubscriberView.as_view(), name='subscriber-add'),
]

