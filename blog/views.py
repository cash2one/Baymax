# coding=utf-8

from django.shortcuts import render

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import utils, forms
from .models import Article, ArticleType, Comment, Tags
import time


def sidebar_data():
    new_arts = Article.objects.all()[:5]
    art_type = ArticleType.objects.all()
    tags = Tags.objects.all()

    return new_arts, art_type, tags


def home(request):
    arts = Article.objects.all()
    sd = sidebar_data()

    return render_to_response('blog/index.html', {'arts': arts,'new_arts':sd[0],'art_types':sd[1],'tags':sd[2]},
                              context_instance=RequestContext(request))


@login_required(login_url="/woodpecker/login/")
def post_article(request):
    if request.method == 'POST':
        form = forms.ArticleForm(request.POST)
        if form.is_valid():
            No = str(time.time()).replace('.', '')
            cd = form.cleaned_data
            Title = cd['Title']
            ArticleTypeId = ArticleType.objects.get(id=1)
            Content = cd['Content']
            Description = cd['Description']
            ReplyNum = 3
            ReadNum = 2
            Status = 1
            Tags = cd['Tags']

            article = Article(No=No, Title=Title, ArticleTypeId=ArticleTypeId, Content=Content,
                              ReplyNum=ReplyNum,
                              ReadNum=ReadNum, Status=Status, Tags=Tags, Description=Description)
            article.save()
            return HttpResponseRedirect('/')
    else:
        form = forms.ArticleForm()
    return render_to_response('blog/post.html', {'form': form},
                              context_instance=RequestContext(request))


def article_detail(request, no):
    art = Article.objects.get(No=no)

    return render_to_response('blog/article.html', {'art': art},
                              context_instance=RequestContext(request))