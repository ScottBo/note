# -*- coding: utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response
from mynote.forms import userInfoForm
from mynote.forms import userLoginForm
from mynote.models import userInfo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
# Create your views here.
def is_user_exist(request):
    if request.method == 'GET' and 'q' in request.GET:
        name=request.GET['q']
        if name is not None and name != '':
            try:
                User.objects.get(username=name)
                error_msg=u'用户名已存在'
            except User.DoesNotExist:
                error_msg=u''
        else:
            error_msg=u"用户名不能为空"
        data = {"error_msg":error_msg}
    return HttpResponse(simplejson.dumps(data,ensure_ascii=False),content_type='application/json')

def user_login(request):
    if request.method == "POST":
        fr=userLoginForm( request.POST )
        if fr.is_valid():
            name = fr.cleaned_data['ul_name']
            pwd = fr.cleaned_data['ul_password']
            user = authenticate( username=name,password=pwd )
            if user is not None:
                if user.is_active:
                    auth.login(request,user);
                    return HttpResponseRedirect("/manage/"+user.username+"/")
                else:
                    return HttpResponse("User is not active!")
            else:
                return HttpResponse("user not exist!!!")
    else:
        fr = userLoginForm()
    return render_to_response("login.html",{"fr":fr},context_instance=RequestContext(request))
def register(request):
    if request.method == "POST":
        fr=userInfoForm(request.POST)
        if fr.is_valid():
            #today=datetime.datetime.today();
            #create_date=today.strftime("%Y-%m-%d %H:%M")
            name=fr.cleaned_data['uif_name']
            #rand_sha=string.join(random.sample('abcdefghijklmnopqrstuvwxyz!@#$%^&*()',10)).replace(' ','')
            password= fr.cleaned_data['uif_password']
            #password=hashlib.md5(rand_sha+password).hexdigest()
            sex=fr.cleaned_data['uif_sex']
            email=fr.cleaned_data['uif_email']
            try:
                user=User.objects.create_user(username=name,password=password,email=email)
                userinfo=userInfo(user_id=user.id,ui_sex=sex)
                userinfo.save()
            except IntegrityError:
                return render_to_response("register.html",{"fr":fr,"error":u"用户名已存在"},context_instance=RequestContext(request))
            #user=userInfo(ui_create_date_time=create_date,ui_rand_sha=rand_sha,ui_last_login_time=create_date,ui_password=password,ui_email=email,ui_name=name,ui_sex=sex)
            #user.save()
            return HttpResponse("Ok")
    else:
        fr=userInfoForm()
    return render_to_response("register.html",{"fr":fr},context_instance=RequestContext(request))
@login_required(login_url='/user_login/')
def note_manage(request,username):
    return render_to_response("manage/index.html",{"username":username},context_instance=RequestContext(request))

def note_add(request):
    return render_to_response("manage/add_note.html",{},context_instance=RequestContext(request))
