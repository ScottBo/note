# -*- coding: utf-8 -*-
from django import forms
from captcha.fields  import CaptchaField
class userLoginForm(forms.Form):
    ul_name = forms.CharField()
    ul_password = forms.CharField( widget=forms.PasswordInput )

class userInfoForm(forms.Form):
    RADIO_CHOICES=((1,"男"),(2,"女"))
    uif_name = forms.CharField( error_messages={'required':'Please enter your name!'} )
    uif_password = forms.CharField( error_messages={'required':'Please enter your password!'}, widget=forms.PasswordInput )
    uif_sex = forms.ChoiceField( widget=forms.RadioSelect, error_messages={'required':'Please select your sex!'},choices=RADIO_CHOICES )
    uif_email = forms.EmailField( error_messages={'required':'Please enter your email!'})
    uif_captcha = CaptchaField()
