from django.http import HttpResponse
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response
from mynote.forms import userInfoForm
from mynote.models import userInfo
import datetime
import random
import string
import hashlib
# Create your views here.
def register(request):
    if request.method == "POST":
        fr=userInfoForm(request.POST)
        if fr.is_valid():
            today=datetime.datetime.today();
            create_date=today.strftime("%Y-%m-%d %H:%M")
            name=fr.cleaned_data['uif_name']
            rand_sha=string.join(random.sample('abcdefghijklmnopqrstuvwxyz!@#$%^&*()',10)).replace(' ','')
            password= fr.cleaned_data['uif_password']
            password=hashlib.md5(rand_sha+password).hexdigest()
            sex=fr.cleaned_data['uif_sex']
            email=fr.cleaned_data['uif_email']
            user=userInfo(ui_create_date_time=create_date,ui_rand_sha=rand_sha,ui_last_login_time=create_date,ui_password=password,ui_email=email,ui_name=name,ui_sex=sex)
            user.save()
            return HttpResponse("Ok")
    else:
        fr=userInfoForm()
    return render_to_response("register.html",{"fr":fr},context_instance=RequestContext(request))
