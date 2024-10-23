###
 # @Author: fuyunyou
 # @Date: 2024-10-22 18:56:39
 # @LastEditors: fuyunyou
 # @LastEditTime: 2024-10-23 10:00:47
 # @Description: 其中包含各种视图函数，处理uers视图中用户的操作逻辑，数据交互
 # @FilePath: \learning_log\users\views.py
###
from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """注册新用户"""
    if request.method !='POST':
        """显示空的注册表单"""
        form=UserCreationForm()
    else:
        """处理写好的表单"""
        form=UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user=form.save()
            #让用户自动登录在重定向到主页
        login(request,new_user)
        return redirect('learning_logs:index')
    
    #显示空表单或指出表单无效
    context={'form':form}
    return render(request,'registration/register.html',context)