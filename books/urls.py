from django.conf.urls import url
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
	url(r'^$', views.index, name='index'),								# http://127.0.0.1:8000/___/
	url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),		# http://127.0.0.1:8000/books/100/
	url(r'^create/', views.create_book, name='create_book'),
	url(r'^update/', views.update_books, name='update_books'),

]

