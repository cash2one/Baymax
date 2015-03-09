# coding=utf-8
from django.db import models

# null：
# If True, Django will store empty values as NULL in the database. Default is False.
# 如果为True，空值将会被存储为NULL，默认为False。
#
# blank：
#     If True, the field is allowed to be blank. Default is False.
#     如果为True，字段允许为空，默认不允许。

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
    CreateTime = models.DateTimeField(null=True)
    UpdateTime = models.DateTimeField(null=True)
    Description = models.TextField(blank=True)


class TestCase(models.Model):
    ModuleId = models.ForeignKey(DeviceModule)
    TestCaseName = models.CharField(max_length=50)
    DisplayName = models.CharField(max_length=50)
    ExecuteCount = models.IntegerField()
    ActivityValue = models.TextField(blank=True)
    TestCaseAction = models.CharField(max_length=100, blank=True)
    TestCaseEntity = models.CharField(max_length=100, blank=True)
    IsEnable = models.BooleanField(default=True)
    CreateTime = models.DateTimeField(null=True)
    UpdateTime = models.DateTimeField(null=True)
    Description = models.TextField(blank=True)
    AloneUse = models.CharField(max_length=50, blank=True)
    IsJoin = models.BooleanField(default=True)


class Task(models.Model):
    TaskName = models.CharField(max_length=50)
    TaskType = models.IntegerField(null=True)
    TaskCount = models.IntegerField()
    TaskState = models.IntegerField()
    Creator = models.ForeignKey(AppUser)
    DeviceType = models.CharField(max_length=50)
    Description = models.TextField(null=True,blank=True)
    CreateTime = models.DateTimeField()
    UpdateTime = models.DateTimeField()
    CreateWay = models.CharField(max_length=50)
    IsShared = models.BooleanField(default=False)


class Result(models.Model):
    TaskId = models.ForeignKey(Task)
    TestCaseId = models.ForeignKey(TestCase)
    DeviceId = models.CharField(max_length=50, blank=True)
    TestResult = models.TextField(blank=True)
    StartTime = models.DateTimeField(blank=True)
    EndTime = models.DateTimeField(blank=True)
    TestResultFile = models.CharField(max_length=50)
    ResultCount = models.IntegerField()
    ValueSettings = models.TextField(blank=True)
    IsEnable = models.BooleanField(default=True)

