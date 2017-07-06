# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from app01 import models
from django.contrib import admin

# Register your models here.
admin.site.register(models.Weibo)
admin.site.register(models.Tags)
admin.site.register(models.Acount)
