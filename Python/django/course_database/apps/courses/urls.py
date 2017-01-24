from django.conf.urls import url
from . import views
# ^ So we can call functions from our routes!
urlpatterns = [
	url(r'^$', views.index),
    url(r'^courses/destroy/(?P<id>\d+)$', views.confirm),
	url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^submit$', views.submit)
]
