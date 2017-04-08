from django.conf.urls import url
from . import views


app_name = 'bloggiz'
urlpatterns = [
    url('', views.ListView.as_view(), name='list'),
]




