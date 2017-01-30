from django.conf.urls import url
from . import views
# ^ So we can call functions from our routes!
urlpatterns = [
	url(r'^result$', views.index),
    url(r'^$', views.generate)
]
