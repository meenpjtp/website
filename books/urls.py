from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	url(r'^$', views.index, name='index'),								# http://127.0.0.1:8000/___/
	url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail')			# http://127.0.0.1:8000/books/100/

]

urlpatterns += staticfiles_urlpatterns()
