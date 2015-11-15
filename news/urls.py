# coding=utf-8
__author__ = 'guguohai@outlook.com'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'news.views.wap_new'),
    url(r'^oschina/', 'news.views.oschina'),
    url(r'^cnbeta/', 'news.views.cnbeta'),
    url(r'^csdn/', 'news.views.csdn'),
    url(r'^wap/', 'news.views.wap_new'),
    url(r'^wap_con/', 'news.views.wap_con'),
    url(r'^wap_menu/', 'news.views.wap_menu'),
    url(r'^wap_result/', 'news.views.wap_result'),

)