from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from djchat import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djchatrooms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   url(r'^register/$',views.chat_register,name="register"),
   url(r'^login/$',views.chat_login,name="login"),
   url(r'^logout/$',views.chat_logout,name="logout"),
)

