from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
	url(r'^ninjas/(?P<color>\w+)$', views.ninjaLocator),
	url(r'^ninjas/$', views.ninjaLocator),
	url(r'^ninjas$', views.ninjaLocator)
]
