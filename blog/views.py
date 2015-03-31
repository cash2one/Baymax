# coding=utf-8

from django.shortcuts import render

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import utils, forms
from .models import Article, ArticleType, Comment


def home(request):
    bing=utils.getBingImg('http://cn.bing.com/')
    arts = Article.objects.all()

    return render_to_response('blog/index.html', {'bing':bing,'arts': arts},
                              context_instance=RequestContext(request))



@login_required(login_url="/woodpecker/login/")
def post_article(request):
    bing=utils.getBingImg('http://cn.bing.com/')
    if request.method == 'POST':
        form = forms.ArticleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Title = cd['Title']
            ArticleTypeId = ArticleType.objects.get(id=1)
            Content = cd['Content']
            ReplyNum = 3
            ReadNum = 2
            Property = 1
            Tags = cd['Tags']

            article = Article(Title=Title, ArticleTypeId=ArticleTypeId, Content=Content, ReplyNum=ReplyNum,
                              ReadNum=ReadNum, Property=Property, Tags=Tags)
            article.save()
            return HttpResponseRedirect('/')
    else:
        form = forms.ArticleForm()
    return render_to_response('blog/post.html', {'bing':bing,'form': form},
                              context_instance=RequestContext(request))