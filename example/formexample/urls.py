__author__ = 'asagli'

try:
    from django.conf.urls import patterns, url
except ImportError:
    # Django < 1.4
    from django.conf.urls.defaults import patterns, url

from formexample.views import *

from django.views.generic import TemplateView

# Blog patterns.
urlpatterns = patterns("example.views",
    url("^$" , TemplateView.as_view(template_name='example/home.html'), name="home"),
    url("^cicu-freecrop/$" , freeCropView, name="cicuExample-freecrop"),
    url("^cicu-fixedratio/$" , fixedRatioView, name="cicuExample-fixedratio"),
    url("^cicu-warningsize/$" , warningSizeView, name="cicuExample-warningsize"),
)
