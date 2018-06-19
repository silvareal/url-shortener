from django.conf.urls import url
from django.contrib import admin
from shorten.views import ShortenCBV, KirrRedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', ShortenCBV.as_view()),
    url(r'(?P<shortcode>[\w-]+)/$', KirrRedirectView.as_view(), name='shortcode')
]
