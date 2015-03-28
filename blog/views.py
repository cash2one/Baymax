# coding=utf-8

from django.shortcuts import render

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import utils


def home(request):
    # return render_to_response("blog/index.html", {"home": ''}, context_instance=RequestContext(request))

    bingimg = utils.getBingImg('http://cn.bing.com/')
    return render_to_response('blog/index.html', {"home": '', 'bingimg': bingimg},
                              context_instance=RequestContext(request))