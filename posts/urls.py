from django.conf.urls import url
from django.contrib import admin


#inplace import
from .views import (
	post_list,	
	post_create,
	post_detail,
	post_list,
	post_update,
	post_delete,
	)

#from posts import views
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', post_list,name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail,name='detail'), #concept of dynamic urls..
    url(r'^(?P<id>\d+)/edit/$', post_update,name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
]

#for more common urls https://github.com/codingforentrepreneurs/guides