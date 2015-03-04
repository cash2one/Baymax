from django.shortcuts import render

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django import forms
from django.template import RequestContext
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render_to_response("app/index.html", {"tasks": tasks},context_instance=RequestContext(request))
    #return render(request,'index.html')

def about(request):
    # tasks = Task.objects.all()
    #return render_to_response("resp.html", {"tasks": tasks})
    return render(request, 'app/about.html',context_instance=RequestContext(request))