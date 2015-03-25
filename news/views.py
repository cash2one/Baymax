# coding=utf-8

from django.shortcuts import render

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import time, urllib2, re, json


def wap(request):
    return render_to_response("news/wap.html", {"testcase": ''}, context_instance=RequestContext(request))


def wap_con(request):
    return render_to_response("news/wap_content.html", {"testcase": ''}, context_instance=RequestContext(request))


def wap_menu(request):
    return render_to_response("news/wap_menu.html", {"testcase": ''}, context_instance=RequestContext(request))


def result_data(request):
    page = request.GET.get('page')
    response_data = []

    temp_data = [{'result': 'Facebook本周举行开发者大会', 'image': 'http://p2.pstatp.com/list/2575/443537243'},
                 {'result': '迪斯尼CEO曾隐瞒乔布斯病情长达三年之久', 'image': 'http://p1.pstatp.com/list/2575/540112485'},
                 {'result': '网络租房比例过半 94%网民怨中介费高', 'image': 'http://p2.pstatp.com/list/2563/3821559120'},
                 {'result': '披着“羊皮”朋友圈谣言 你还能明辨吗', 'image': 'http://p2.pstatp.com/list/2551/405337174'},
                 {'result': '网友免费在线听歌，环球等唱片公司', 'image': 'http://p1.pstatp.com/list/2540/6698892493'}]

    for i in range(0, 5):
        response_data.append(temp_data)

    response_data.append(None)

    return HttpResponse(json.dumps(response_data[int(page)]), content_type="application/json")