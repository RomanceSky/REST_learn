# -*- coding: utf-8 -*-
from django.conf.urls import url
from snippets import views

from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include


urlpatterns = [
#    url(r'^snippets/$', views.snippet_list),
#   url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
#: 改为基于类的视图对应的url
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'users/$', views.UserList.as_view()),
    url(r'users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
#:api
    url(r'apitest/$', views.apitestView),

 
]

#: 认证和权限-在浏览器API中添加登录
#: 在urls.py底部为API添加一个包括登录和退出视图的url样式


urlpatterns +=[
    url(r'^api-auth/', include('rest_framework.urls',
    				namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
