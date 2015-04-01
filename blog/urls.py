# coding=utf-8
__author__ = 'guguohai@outlook.com'

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home'),
    url(r'^home/$', 'blog.views.home'),
    url(r'^post/$', 'blog.views.post_article'),
    url(r'^article/(?P<no>\w+)/$', 'blog.views.article_detail'),
    url(r'^articles/(?P<name>\w+)/$', 'blog.views.article_list'),

)