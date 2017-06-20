# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from logs.models import Logs

def userLogin(request):
    if request.user.is_authenticated():
        return redirect('dashboard')
    if request.method == 'POST':
        data = request.POST
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return render(request,'login.html',{"error":"check your credentials"})
    return render(request,'login.html')

@staff_member_required(redirect_field_name='dashboard',login_url='dashboard')
@login_required(login_url='userLogin')
def usersView(request):
    users = User.objects.all()
    return render(request,'users.html',{'sysusers':users})

@staff_member_required(redirect_field_name='dashboard',login_url='dashboard')
@login_required(login_url='userLogin')
def userRegister(request):
    if request.method == 'POST':
        data = request.POST
        staff = True if 'staff' in data else False
        user = User.objects.create_user(username=data['username'],
        email=data['email'],
        password=data['password'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        is_staff=staff)
        Logs(user_logged=request.user,function='users',message='Create %s user' % data['username']).save()
        return redirect('usersView')
    return render(request,'userRegister.html')

@staff_member_required(redirect_field_name='dashboard',login_url='dashboard')
@login_required(login_url='userLogin')
def userEdit(request,sysuser_id):
    sysuser = User.objects.get(id=sysuser_id)
    if request.method == 'POST':
        data = request.POST
        staff = True if 'staff' in data else False
        sysuser.email= data['email']
        sysuser.first_name= data['first_name']
        sysuser.last_name= data['last_name']
        sysuser.is_staff= staff
        sysuser.save(update_fields=["email","first_name","last_name","is_staff"])
        Logs(user_logged=request.user,function='users',message='Edit %s user' % sysuser.username).save()
        return redirect('usersView')
    return render(request,'userRegister.html',{'sysuser':sysuser})

@login_required(login_url='userLogin')
def userPassword(request):
    sysuser = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        data = request.POST
        if sysuser.check_password(data['actual_password']) and data['new_password'] == data['conf_password']:
            sysuser.set_password(data['new_password'])
            sysuser.save()
            Logs(user_logged=request.user,function='users',message='Change password').save()
        return redirect('dashboard')
    return render(request,'userPassword.html')

@staff_member_required(redirect_field_name='dashboard',login_url='dashboard')
@login_required(login_url='userLogin')
def userDelete(request,sysuser_id):
    if request.user.id != int(sysuser_id):
        user = User.objects.get(id=sysuser_id)
        Logs(user_logged=request.user,function='users',message='Delete %s user' % user.username).save()
        user.delete()
    return redirect('usersView')

@login_required(login_url='userLogin')
def userLogout(request):
    logout(request)
    return redirect('userLogin')
