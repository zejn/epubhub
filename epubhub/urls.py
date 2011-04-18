from django.conf.urls.defaults import *
from django.views.generic import list_detail
from epubhub.models import Ebook

ebook_info = {
    'queryset': Ebook.objects.all(),
}

urlpatterns = patterns('epubhub.views',
    url(r'^b/get/(?P<object_id>\d+)/$', 'get_ebook', name='get_ebook'),
    url(r'^b/get/mobi/(?P<object_id>\d+)/$', 'ebook_convert_mobi', name='ebook_convert_mobi'),
    url(r'^b/$', 'ebook_list', name='ebook_list'),
)

urlpatterns += patterns('',
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/b/'}),
)
