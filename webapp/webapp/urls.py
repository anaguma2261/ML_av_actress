from django.conf.urls import patterns, include, url
from django.contrib import admin
from similar_actress import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^show/(?P<img_id>\d+)/$', views.show, name='show'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^admin/', include(admin.site.urls)),
)
