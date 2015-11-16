# coding=utf-8
from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# null：
# If True, Django will store empty values as NULL in the database. Default is False.
# 如果为True，空值将会被存储为NULL，默认为False。
#
# blank：
# If True, the field is allowed to be blank. Default is False.
# 如果为True，字段允许为空，默认不允许。

class Team(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'team'


class User(AbstractUser):
    department = models.CharField(max_length=100)
    team = models.ForeignKey(Team)


# class User(models.Model):
#     name = models.CharField(max_length=50)
#     true_name = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     email = models.EmailField(blank=True)
#     team = models.ForeignKey(Team)
#
#     class Meta:
#         db_table = 'user'


class Role(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    Users = models.ManyToManyField(User, through='User_Role')  # 注意多了through参数

    class Meta:
        db_table = 'role'


class User_Role(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    role = models.ForeignKey(Role)

    class Meta:
        db_table = 'user_role'
        unique_together = ("user", "role")  # 复合主键


class PermissionType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'permissiontype'


class Permission(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    type = models.ForeignKey(PermissionType)
    roles = models.ManyToManyField(Role, through='Role_Permission')

    class Meta:
        db_table = 'permission'


class Role_Permission(models.Model):
    role = models.ForeignKey(Role)
    permission = models.ForeignKey(Permission)

    class Meta:
        db_table = 'role_permission'
        unique_together = ("role", "permission")  # 复合主键


class ProductType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'producttype'


class Product(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(ProductType)
    team = models.ForeignKey(Team)

    class Meta:
        db_table = 'product'


class Module(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product)

    class Meta:
        db_table = 'module'


class TestCase(models.Model):
    name = models.CharField(max_length=100)
    module = models.ForeignKey(Module)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        db_table = 'testcase'


class Task(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product)
    type = models.IntegerField(default=1)  # 1、串行，2、并行
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    testcases = models.ManyToManyField(TestCase, through='Task_TestCase')

    class Meta:
        db_table = 'task'


class Task_TestCase(models.Model):
    task = models.ForeignKey(Task)
    testcase = models.ForeignKey(TestCase)

    class Meta:
        db_table = 'result'
        unique_together = ("task", "testcase")  # 复合主键


class Bug(models.Model):
    name = models.CharField(max_length=100)
    #task_testCases = models.ManyToManyField(Task_TestCase, through='Task_TestCase_Bug')
    testcases = models.ManyToManyField(TestCase, through='Task_TestCase_Bug')
    tasks = models.ManyToManyField(Task, through='Task_TestCase_Bug')

    class Meta:
        db_table = 'bug'


class Task_TestCase_Bug(models.Model):
    task = models.ForeignKey(Task)
    testcase = models.ForeignKey(TestCase)
    bug = models.ForeignKey(Bug)

    class Meta:
        db_table = 'result_bug'
        unique_together = ("task", "testcase", "bug")  # 复合主键

# class Module(models.Model):
#     ModuleName = models.CharField(max_length=300)
#     DisplayName = models.CharField(max_length=300)
#     IsEnable = models.BooleanField(default=True)
#     CreateTime = models.DateTimeField(null=True, auto_now_add=True)
#     UpdateTime = models.DateTimeField(null=True, auto_now=True)
#     Description = models.TextField(null=True, blank=True)
#
#     def __unicode__(self):
#         return u'%s(%s)' % (self.DisplayName, self.ModuleName)
#
#
# class TestCase(models.Model):
#     ModuleId = models.ForeignKey(Module)
#     TestCaseName = models.CharField(max_length=50)
#     DisplayName = models.CharField(max_length=50)
#     ExecuteCount = models.IntegerField()
#     ActivityValue = models.TextField(null=True, blank=True)
#     TestCaseAction = models.CharField(max_length=100, null=True, blank=True)
#     TestCaseEntity = models.CharField(max_length=100, null=True, blank=True)
#     IsEnable = models.BooleanField(default=True)
#     CreateTime = models.DateTimeField(null=True, auto_now_add=True)
#     UpdateTime = models.DateTimeField(null=True, auto_now=True)
#     Description = models.TextField(null=True, blank=True)
#     AloneUse = models.CharField(max_length=50, null=True, blank=True)
#     IsJoin = models.BooleanField(default=True)
#
#
# class Task(models.Model):
#     TaskName = models.CharField(max_length=50)
#     TaskType = models.IntegerField(default=1)  # 1、串行，2、并行
#     TaskCount = models.IntegerField()
#     TaskState = models.IntegerField()
#     Creator = models.ForeignKey(AppUser)
#     DeviceType = models.IntegerField(default=1)  # 1、web app，2、android，3、iOS
#     Description = models.TextField(null=True, blank=True)
#     CreateTime = models.DateTimeField(auto_now_add=True)
#     UpdateTime = models.DateTimeField(auto_now=True)
#     CreateWay = models.IntegerField(default=1)  # 任务有在app上创建和web上创建
#     IsShared = models.BooleanField(default=1)  # 是否共享
#
#
# class Result(models.Model):
#     TaskId = models.ForeignKey(Task)
#     TestCaseId = models.ForeignKey(TestCase)
#     DeviceId = models.CharField(max_length=50, null=True, blank=True)
#     TestResult = models.TextField(null=True, blank=True)
#     StartTime = models.DateTimeField(null=True)
#     EndTime = models.DateTimeField(null=True)
#     TestResultFile = models.CharField(max_length=50)
#     ResultCount = models.IntegerField()
#     ValueSettings = models.TextField(null=True, blank=True)
#     IsEnable = models.BooleanField(default=True)
