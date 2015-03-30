from django.db import models


class ArticleType(models.Model):
    TypeName = models.CharField(max_length=50)
    TypeDescription = models.TextField(null=True, blank=True)


class Article(models.Model):
    Title = models.CharField(max_length=150)
    ArticleTypeId = models.ForeignKey(ArticleType)
    PostTime = models.DateTimeField(auto_now_add=True)
    UpdateTime = models.DateTimeField(auto_now=True)
    Content = models.TextField(null=True, blank=True)
    ReplyNum = models.IntegerField(default=0)
    ReadNum = models.IntegerField(default=0)
    Property = models.IntegerField(default=0)
    Tags = models.CharField(max_length=150)


class Comment(models.Model):
    ArticleId = models.ForeignKey(Article)
    NickName = models.CharField(max_length=30)
    Email = models.CharField(max_length=50)
    Content = models.TextField(null=True, blank=True)
    ReplyContent = models.TextField(null=True, blank=True)
    ReplyTime = models.DateTimeField()
    FromIp = models.CharField(max_length=20, null=True, blank=True)
    Property = models.IntegerField(default=0)
    CreateTime = models.DateTimeField()