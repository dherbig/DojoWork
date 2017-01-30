from django.conf.urls import url
from . import views
# ^ So we can call functions from our routes!
urlpatterns = [
    url(r'^confirm/(?P<id>\d+)$', views.confirm, name='confirm'),
	url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^submit$', views.submit, name='submit'),
	url(r'^users_courses$', views.users_courses, name='users_courses')
]
