# -*- coding: utf-8 -*-
from django import forms
class userInfoForm(forms.Form):
    RADIO_CHOICES=((1,"man"),(2,"woman"))
    uif_name = forms.CharField( label=u"用户名" )
    uif_password = forms.CharField( label=u"密码", widget=forms.PasswordInput )
    uif_sex = forms.ChoiceField( label=u"性别",choices=RADIO_CHOICES )
    uif_email = forms.EmailField( label=u"Email" )
