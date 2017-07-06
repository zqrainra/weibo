#coding:utf8
from django import forms
from django.contrib.auth import models as a_models
from app01 import models


class ChangeProfileForm(forms.ModelForm):
    class Meta:
        model = a_models.User
        fields = ['first_name','last_name']
    # username = forms.CharField(required=True,max_length=100,error_messages=u'用户名是必须的')
    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)
    # email = forms.CharField(max_length=100)

class AcountForm(forms.ModelForm):
    class Meta:
        model = models.Acount
        fields = ['name','brief']
