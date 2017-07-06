# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth import models
from .forms import ChangeProfileForm
from django.views.decorators.cache import cache_page
import json
from app01 import models
# Create your views here.


def change_profile(request):
    user = models.User.objects.get(username=request.user.username)
    context = {}
    if request.method == 'GET':
        form = ChangeProfileForm(instance=user)
    elif request.method == 'POST':
        form = ChangeProfileForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            form = ChangeProfileForm()
            context['success'] = True
    context['form'] = form
    return render(request,'message/change_profile.html',context=context)

def show_acount(request):
    if request.method == 'GET':
        users = models.Acount.objects.all()


    context = {'users':users}
    return render(request,'message/show_acount.html',context=context)