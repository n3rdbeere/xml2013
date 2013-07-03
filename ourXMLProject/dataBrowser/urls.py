from django.conf.urls import patterns, url

from dataBrowser import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^openURI/$', views.openUri, name='openUri'),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
<<<<<<< HEAD
        {'document_root': '/home/user/xml2013/ourXMLProject/dataBrowser/templates'})
=======
        {'document_root': '/home/user/git/xml2013/ourXMLProject/dataBrowser/templates'})
>>>>>>> master
)
