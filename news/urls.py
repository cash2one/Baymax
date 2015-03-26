# coding=utf-8
__author__ = 'guguohai@outlook.com'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'news.views.wap'),
    url(r'^wap/', 'news.views.wap'),
    url(r'^wap_con/', 'news.views.wap_con'),
    url(r'^result_data/$', 'news.views.result_data'),
    url(r'^wap_menu/', 'news.views.wap_menu'),
    url(r'^wap_new/', 'news.views.wap_new'),
    url(r'^wap_new_json/', 'news.views.wap_new_json'),

)