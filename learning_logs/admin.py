###
 # @Author: fuyunyou
 # @Date: 2024-10-22 11:26:41
 # @LastEditors: fuyunyou
 # @LastEditTime: 2024-10-22 13:37:39
 # @Description: 
 # @FilePath: \learning_log\learning_logs\admin.py
###
from django.contrib import admin

from .models import Topic,Entry

admin.site.register(Topic)
admin.site.register(Entry)