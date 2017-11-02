from django.conf.urls import url
from . import views

app_name = 'demo'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^grade/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]