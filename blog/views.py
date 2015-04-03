# coding=utf-8

from django.shortcuts import render

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import utils, forms
from .models import Article, ArticleType, Comment, Tags, TagsMap
import time


def sidebar_data():
    new_arts = Article.objects.all()[:5]
    art_types = ArticleType.objects.all()
    tags = Tags.objects.all()

    return {'new_arts': new_arts, 'art_types': art_types, 'tags': tags}


def home(request):
    sd = sidebar_data()

    result = {'arts': Article.objects.all()}

    return render_to_response('blog/index.html', dict(result, **sd),
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
            tag_strs = cd['Tags'].split(',')

            article = Article(No=No, Title=Title, ArticleTypeId=ArticleTypeId, Content=Content,
                              ReplyNum=ReplyNum,
                              ReadNum=ReadNum, Status=Status, Description=Description)
            # article.save()

            # 取出标签名
            tags = Tags.objects.all()
            tag_names = []
            for t in tags:
                tag_names.append(t.TagName)


            #比较后存入
            for t in tag_strs:
                tag = None
                if t not in tag_names:
                    tag = Tags(TagName=t, Quote=1)
                else:
                    tag = Tags.objects.get(TagName=t)
                    tag.Quote += 1

                tm = TagsMap(article, tag)
                tm.save()

            return HttpResponseRedirect('/')
    else:
        form = forms.ArticleForm()
    return render_to_response('blog/post.html', {'form': form},
                              context_instance=RequestContext(request))


def article_detail(request, no):
    result = {'art': Article.objects.get(No=no)}
    sd = sidebar_data()
    return render_to_response('blog/article.html', dict(result, **sd),
                              context_instance=RequestContext(request))


def articles_by_type(request, name):
    art_type = ArticleType.objects.get(TypeName=name)
    result = {'arts': Article.objects.filter(ArticleTypeId=art_type.id)}
    sd = sidebar_data()

    return render_to_response('blog/article_list.html', dict(result, **sd),
                              context_instance=RequestContext(request))


def articles_by_tag(request, name):
    tag = Tags.objects.get(TagName=name)
    tag_map = TagsMap.objects.filter(TagsId=tag.id)

    art_list = []

    for tm in tag_map:
        art_list.append(Article.objects.get(id=tm.ArticleId))

    result = {'arts': art_list}
    sd = sidebar_data()
    return render_to_response('blog/article_list.html', dict(result, **sd),
                              context_instance=RequestContext(request))



