# coding=utf-8
__author__ = 'guguohai@outlook.com'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home'),
    url(r'^home/$', 'blog.views.home'),
    url(r'^post/$', 'blog.views.post_article'),

)