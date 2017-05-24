#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author ==>Adair-jie
# Email  ==>0101adair@gmail.com
# Github ==>https://github.com/zhu-jie
import  xadmin

from .models import UserAsk,CourseComments,UserFavorite,UserMessage,UserCourse


class UserAskAdmin(object):
    list_display = ['name','mobile','add_time']
    search_fields = ['name','mobile']
    list_filter = ['name','mobile','add_time'] #非常强大的过滤器


class CourseCommentsAdmin(object):
    list_display = ['user','course','comments','add_time']
    search_fields = ['user','course','comments']
    list_filter = ['user','course','comments','add_time']


class UserFavoriteAdmin(object):
    list_display = ['user','course','fav_id','fav_type','add_time']
    search_fields = ['user','course','fav_id','fav_type']
    list_filter = ['user','course','fav_id','fav_type','add_time']


class UserMessageAdmin(object):
    list_display = ['user','meseage','has_read','add_time']
    search_fields = ['user','meseage','has_read']
    list_filter = ['user','meseage','has_read','add_time']


class UserCourseAdmin(object):
    list_display = ['user','course','add_time']
    search_fields = ['user','course','fav_id','fav_type']
    list_filter = ['user','course','fav_id','fav_type','add_time']


xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)