from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.db import connection
from .s3_handler import S3Handler
from openpyxl import load_workbook, Workbook
from django.contrib import messages
import requests
from urllib.parse import urlparse
import logging
from django.forms import ModelForm
from django import forms
from django.utils import timezone


from .models import pm,pm2

from .forms import ListForm

class pm1(View):
  
    def get(self, request):
        all_items=pm.objects.all
        return  render(request,'pages/mtd/apis/pm.html',{'all_item': all_items})

    def post(self, request):
        Sprint= request.POST.get('Sprint')
        Asignee= request.POST.get('Asignee')
        Status= request.POST.get('Status')
        Epic= request.POST.get('Epic')
        Priority= request.POST.get('Priority')
        Estimation= request.POST.get('Estimation')
        l1=pm(src_sys_id='pm1',
            sprint=Sprint,
            asignee=Asignee,
            status=Status,
            epic=Epic,
            priority = Priority,
            estimation =Estimation)
        l1.save()
        all_items=pm.objects.all
        return  render(request,'pages/mtd/apis/pm.html',{'all_item': all_items})

class pm3(View):
  
    def get(self, request):
        all_items=pm2.objects.all
        return  render(request,'pages/mtd/apis/pm.html',{'all_item': all_items})

    def post(self, request):
        Sprint= request.POST.get('Sprint')
        Asignee= request.POST.get('Asignee')
        Status= request.POST.get('Status')
        Epic= request.POST.get('Epic')
        Priority= request.POST.get('Priority')
        Estimation= request.POST.get('Estimation')
        l1=pm2(src_sys_id='pm2',
            sprint=Sprint,
            asignee=Asignee,
            status=Status,
            epic=Epic,
            priority = Priority,
            estimation =Estimation)
        l1.save()
        all_items=pm2.objects.all
        return  render(request,'pages/mtd/apis/pm.html',{'all_item': all_items})

class about(View):
  
    def get(self, request):
        all_items=pm.objects.all
        return  render(request,'pages/mtd/apis/pm.html',{'all_item': all_items})

class edit(View):
  
    def get(self, request):
        all_items=pm.objects.all
        return  render(request,'pages/mtd/apis/pm.html',{'all_item': all_items})

class cross_on(View):
  
    def get(self, request):
        all_items=pm.objects.all
        return  render(request,'pages/mtd/apis/pm.html',{'all_item': all_items})

class cross_off(View):
  
    def get(self, request, list_id):
        all_items=pm.objects.get(pk=list_id)
        #all_items=pm.objects.all
        print ('cross_off id:' + str(list_id))
        return  render(request,'pages/mtd/apis/pm.html',{'all_item': all_items})

class delete(View):
  
    def get(self, request,list_id):
        item=pm.objects.get(pk=list_id)
        item.delete()
        messages.success(request,('Item has been deleted:'))
        #return redirect('home')
        all_items=pm.objects.all

        return  render(request,'pages/mtd/apis/pm.html',{'all_item': all_items})

class about2(View):
  
    def get(self, request):
        all_items=pm2.objects.all
        return  render(request,'pages/mtd/apis/pm2.html',{'all_item': all_items})

class edit2(View):
  
    def get(self, request):
        all_items=pm2.objects.all
        return  render(request,'pages/mtd/apis/pm2.html',{'all_item': all_items})

class cross_on2(View):
  
    def get(self, request):
        all_items=pm2.objects.all
        return  render(request,'pages/mtd/apis/pm2.html',{'all_item': all_items})

class cross_off2(View):
  
    def get(self, request, list_id):
        all_items=pm2.objects.get(pk=list_id)
        #all_items=pm.objects.all
        print ('cross_off id:' + str(list_id))
        return  render(request,'pages/mtd/apis/pm2.html',{'all_item': all_items})

class delete2(View):
  
    def get(self, request):
        all_items=pm2.objects.all
        return  render(request,'pages/mtd/apis/pm2.html',{'all_item': all_items})
