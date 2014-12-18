from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import djchat


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djchatrooms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^chat/', include('djchat.urls')),
    url(r'^chat/', include('chatrooms.urls'),name='home'),
)

# urlpatterns += staticfiles_urlpatterns()

