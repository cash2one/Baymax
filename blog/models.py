from django.db import models

class Article(models.Model):
    UserName = models.CharField(max_length=50)
    DisplayName = models.CharField(max_length=50)
    UserPassword = models.CharField(max_length=50)
    Email = models.CharField(max_length=100, blank=True)
    UserDefined = models.TextField(blank=True)