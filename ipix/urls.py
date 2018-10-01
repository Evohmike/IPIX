from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.ipix,name='Home'),
    url(r'^search/', views.search_category, name='search_category'),
    url(r'^location/(\d+)', views.filter_by_location, name='location_filter'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
