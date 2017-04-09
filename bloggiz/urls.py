from django.conf.urls import url
from . import views


app_name = 'bloggiz'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='list'),
    url(r'(?P<slug>[-\w]+)/$', views.PostView.as_view(), name='detail'),
]




