from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('books.urls'))  #http://127.0.0.1:8000/ after / don't have books
]
