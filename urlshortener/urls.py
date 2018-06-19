from django.conf.urls import url
from django.contrib import admin
from shorten.views import ShortenCBV, home_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', ShortenCBV.as_view()),
]
