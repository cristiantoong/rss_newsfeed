from django.contrib import admin
from django.urls import path
from rss.views import rss_view, search_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rss/', rss_view, name='rss'),
    path('search_url/', search_url),
]
