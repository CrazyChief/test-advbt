from django.conf.urls import url
from .views import CyView


app_name = 'currency'
urlpatterns = [
    url(r'^set-currency/$', CyView.as_view(), name='set-currency'),
]
