#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author ==>Adair-jie
# Email  ==>0101adair@gmail.com
# Github ==>https://github.com/zhu-jie
import  xadmin

from .models import EmailVerifyRecord
class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)