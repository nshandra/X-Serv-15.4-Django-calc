from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(\d+|\d+\.\d*)([-\+*/])(\d+|\d+.\d*)$', 'calc.views.calc_app'),
    url(r'^.*$', 'calc.views.not_found')
)
