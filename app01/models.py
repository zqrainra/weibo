# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
import os
from app01.widget.get_img import   gen_default_head_img

# Create your models here.
class Weibo(models.Model):
    wb_type_choices = (
        (0, 'new'),
        (1, 'forward'),
        (2, 'collect'),
    )
    wb_type = models.IntegerField(choices=wb_type_choices, default=0)
    forward_or_collect_from = models.ForeignKey('self', related_name="forward_or_collects", blank=True, null=True)
    user = models.ForeignKey('Acount')
    text = models.CharField(max_length=140)
    pictures_link_id = models.CharField(max_length=128, blank=True, null=True)
    video_link_id = models.CharField(max_length=128, blank=True, null=True)
    perm_choice = ((0, 'public'),
                   (1, 'private'),
                   (2, 'friends'))
    perm = models.IntegerField(choices=perm_choice, default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text


class Tags(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Acount(models.Model):
    sex_choice = ((1,'male'),(2,'famale'))

    user = models.OneToOneField(User)
    name = models.CharField(max_length=64)
    brief = models.CharField(max_length=255,blank=True)
    age = models.IntegerField(blank=True)
    sex = models.IntegerField(choices=sex_choice,default=1)
    email = models.EmailField(max_length=255)
    tags = models.ManyToManyField(Tags)
    head_img = models.ImageField(upload_to='head_img/%Y/%m/%d',default='default_image/%s' % gen_default_head_img(os.path.join(settings.MEDIA_ROOT,settings.DEFAULT_HEAD_IMAGE_DIR)))
    follow_list = models.ManyToManyField('self',blank=True,related_name='my_followers',symmetrical=False)


    def __unicode__(self):
        return self.name

