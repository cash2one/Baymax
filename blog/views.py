# coding=utf-8

from django.shortcuts import render

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import utils
from .models import Article,ArticleType,Comment


def home(request):
    articles = Article.objects.all()
    return render_to_response('blog/index.html', {"home": '', 'articles': articles},
                              context_instance=RequestContext(request))