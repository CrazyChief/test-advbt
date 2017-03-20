from django.conf.urls import url
from . import views


app_name = 'contacts'
urlpatterns = [
    url(r'^$', views.ReviewCreate.as_view(), name='index'),
]














