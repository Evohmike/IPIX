from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.ipix,name='Home'),
    # url(r'^image/(?P<category_name>\w+)/(?P<image_id>\d+)',views.single_image, name='art'),

]