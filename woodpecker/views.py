# coding=utf-8

from django.shortcuts import render

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib import auth
from .forms import TaskForm, LoginForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import Task, TestCase, AppUser, DeviceModule
from django.contrib.auth.decorators import login_required
import time, urllib2, re, json


@login_required(login_url="/woodpecker/login/")
def index(request):
    tasks = Task.objects.all()
    return render_to_response("woodpecker/index.html", {"tasks": tasks}, context_instance=RequestContext(request))
    # return render(request,'index.html')


def getBingImg(url):
    re_img = re.compile(r'(?<=g_img=\{url:\').*?(?=.jpg)')
    html = urllib2.urlopen(url).read()

    match = re_img.search(html)
    if match:
        return match.group() + '.jpg'


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        bingimg = getBingImg('http://cn.bing.com/')
        return render_to_response('woodpecker/login.html', RequestContext(request, {'form': form, 'bingimg': bingimg}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('woodpecker/index.html', RequestContext(request))
            else:
                return render_to_response('woodpecker/login.html',
                                          RequestContext(request, {'form': form, 'password_is_wrong': True}))
        else:
            return render_to_response('woodpecker/login.html', RequestContext(request, {'form': form, }))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/woodpecker/login/")


@login_required(login_url="/woodpecker/login/")
def about(request):
    # tasks = Task.objects.all()
    # return render_to_response("resp.html", {"tasks": tasks})
    return render(request, 'woodpecker/about.html', context_instance=RequestContext(request))


@login_required(login_url="/woodpecker/login/")
def task(request):
    tasks = Task.objects.all()
    # return render_to_response("app/task.html", {"tasks": tasks},context_instance=RequestContext(request))

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            task_name = cd['TaskName']
            task_Type = cd['TaskType']
            task_Count = cd['TaskCount']
            task_State = 1
            creator = AppUser.objects.get(id=1)
            deviceType = cd['DeviceType']
            description = cd['Description']
            createTime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            updateTime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            createWay = 'web'
            isShared = cd['IsShared']
            task = Task(TaskName=task_name, TaskType=task_Type, TaskCount=task_Count, TaskState=task_State,
                        Creator=creator, DeviceType=deviceType, Description=description, CreateTime=createTime,
                        UpdateTime=updateTime, CreateWay=createWay,
                        IsShared=isShared)
            task.save()
            # id = Task.objects.order_by('-publish_time')[0].id
            return HttpResponseRedirect('http://www.baidu.com')
    else:
        form = TaskForm()
    return render_to_response('woodpecker/task.html', {'tasks': tasks, 'form': form}, context_instance=RequestContext(request))


@login_required(login_url="/woodpecker/login/")
def device_module(request):
    module = request.GET.get('module')
    devices = DeviceModule.objects.all()
    # devices = DeviceModule.objects.filter(id=2)

    # if m_nav is not None:
    return render_to_response("woodpecker/device.html", {"devices": devices, 'module': module, 'url_path': request.path},
                              context_instance=RequestContext(request))


@login_required(login_url="/woodpecker/login/")
def test_case(request):
    cases = TestCase.objects.all()
    sub_nav = request.GET.get('sub_nav')
    return render_to_response("woodpecker/testcase.html", {"testcase": cases, 'sub_nav': sub_nav, 'url_path': request.path},
                              context_instance=RequestContext(request))
