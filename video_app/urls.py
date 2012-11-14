from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('video_app.views',
    url(r'^list/$', 'list', name='list'),
)
