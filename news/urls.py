# coding=utf-8
__author__ = 'guguohai@outlook.com'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'app.views.wap'),
    url(r'^wap/', 'app.views.wap'),
    url(r'^result_data/$', 'app.views.result_data'),
    url(r'^wap_menu/', 'app.views.wap_menu'),

)