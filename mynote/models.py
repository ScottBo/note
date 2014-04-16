# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#用户表
class userInfo(models.Model):
    user = models.OneToOneField(User)
    ui_sex = models.IntegerField()

#笔记所属类目
class noteCate(models.Model):
    nc_name = models.CharField( max_length=100 )
    nc_num = models.IntegerField()

#笔记的tag
class noteTag(models.Model):
    nt_name = models.CharField( max_length=100 )
    nt_num = models.IntegerField()

#笔记
class noteBean(models.Model):
    nb_user = models.ForeignKey( userInfo )
    nb_title = models.CharField( max_length=100 )
    nb_content = models.TextField()
    nb_public = models.IntegerField()#文章的权限
    nb_cate = models.ForeignKey( noteCate )
    nb_tag = models.ManyToManyField( noteTag )
    nb_status = models.IntegerField()
    nb_review_num = models.IntegerField()
    nb_access_num = models.IntegerField()
    nb_up = models.IntegerField()
    nb_down = models.IntegerField()
    nb_date_time = models.DateTimeField()


#笔记评论,对评论进行评论暂时不加
class noteReview(models.Model):
    nr_user = models.ForeignKey( userInfo )
    nr_content = models.TextField()
    nr_date_time = models.DateTimeField()
    nr_up = models.IntegerField()
    nr_down = models.IntegerField()

