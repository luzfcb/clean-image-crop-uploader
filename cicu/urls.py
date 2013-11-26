try:
    from django.conf.urls import patterns, url
except ImportError:
    # Django < 1.4
    from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('cicu.views',
    url(r'^$', 'upload', name='ajax-upload'),
    url(r'^crop/$', 'crop', name='cicu-crop'),
)
