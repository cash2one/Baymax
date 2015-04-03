# coding=utf-8
from django.db import models

# null：
# If True, Django will store empty values as NULL in the database. Default is False.
# 如果为True，空值将会被存储为NULL，默认为False。
#
# blank：
# If True, the field is allowed to be blank. Default is False.
# 如果为True，字段允许为空，默认不允许。

class AppUser(models.Model):
    UserName = models.CharField(max_length=50)
    DisplayName = models.CharField(max_length=50)
    UserPassword = models.CharField(max_length=50)
    Email = models.CharField(max_length=100, blank=True)
    UserDefined = models.TextField(blank=True)


class DeviceModule(models.Model):
    ModuleName = models.CharField(max_length=300)
    DisplayName = models.CharField(max_length=300)
    IsEnable = models.BooleanField(default=True)
    CreateTime = models.DateTimeField(null=True, auto_now_add=True)
    UpdateTime = models.DateTimeField(null=True, auto_now=True)
    Description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u'%s(%s)' % (self.DisplayName, self.ModuleName)


class TestCase(models.Model):
    ModuleId = models.ForeignKey(DeviceModule)
    TestCaseName = models.CharField(max_length=50)
    DisplayName = models.CharField(max_length=50)
    ExecuteCount = models.IntegerField()
    ActivityValue = models.TextField(null=True, blank=True)
    TestCaseAction = models.CharField(max_length=100, null=True, blank=True)
    TestCaseEntity = models.CharField(max_length=100, null=True, blank=True)
    IsEnable = models.BooleanField(default=True)
    CreateTime = models.DateTimeField(null=True, auto_now_add=True)
    UpdateTime = models.DateTimeField(null=True, auto_now=True)
    Description = models.TextField(null=True, blank=True)
    AloneUse = models.CharField(max_length=50, null=True, blank=True)
    IsJoin = models.BooleanField(default=True)


class Task(models.Model):
    TaskName = models.CharField(max_length=50)
    TaskType = models.IntegerField(default=1)  # 1、串行，2、并行
    TaskCount = models.IntegerField()
    TaskState = models.IntegerField()
    Creator = models.ForeignKey(AppUser)
    DeviceType = models.IntegerField(default=1)  # 1、web app，2、android，3、iOS
    Description = models.TextField(null=True, blank=True)
    CreateTime = models.DateTimeField(auto_now_add=True)
    UpdateTime = models.DateTimeField(auto_now=True)
    CreateWay = models.IntegerField(default=1)  # 任务有在app上创建和web上创建
    IsShared = models.BooleanField(default=1)  # 是否共享


class Result(models.Model):
    TaskId = models.ForeignKey(Task)
    TestCaseId = models.ForeignKey(TestCase)
    DeviceId = models.CharField(max_length=50, null=True, blank=True)
    TestResult = models.TextField(null=True, blank=True)
    StartTime = models.DateTimeField(null=True)
    EndTime = models.DateTimeField(null=True)
    TestResultFile = models.CharField(max_length=50)
    ResultCount = models.IntegerField()
    ValueSettings = models.TextField(null=True, blank=True)
    IsEnable = models.BooleanField(default=True)

