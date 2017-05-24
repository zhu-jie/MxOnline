#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Author ==>Adair-jie
# Email  ==>0101adair@gmail.com
# Github ==>https://github.com/zhu-jie
import xadmin

from .models import Course,Lesson,Video,CourseResource


class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_times','students','fav_nums','image','click_nums','add_time']
    search_fields = ['name','desc','detail','degree','students','fav_nums','click_nums']
    list_filter = ['name','desc','detail','degree','learn_times','students','fav_nums','click_nums','add_time']


class LessonAdmin(object):
    list_display = ['course','name','add_time']
    search_fields =['course','name']
    list_filter = ['course__name','name','add_time'] #此处的course__name代表着外键关联的显示


class VideoAdmin(object):
    list_display = ['lesson','name','add_time']
    search_fields = ['lesson','name']
    list_filter = ['lesson__course','name','add_time']


class CourseResourceAdmin(object):
    list_display = ['course','name','download','add_time']
    search_fields = ['course','name','download']
    list_filter = ['course','name','download','add_time']

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)


