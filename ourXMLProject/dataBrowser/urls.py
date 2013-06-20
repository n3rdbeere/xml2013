from django.conf.urls import patterns, url

from dataBrowser import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^openURI/$', views.open, name='open'),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/xmlproject/xml2013/ourXMLProject/dataBrowser/templates'})
)
