from django.conf.urls import url
from . import views
# ^ So we can call functions from our routes!
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register$', views.register, name='register'),
	url(r'^login$', views.login, name='login'),
	url(r'^success$', views.success, name='success'),
	url(r'^logout$', views.logout, name='logout')
]
