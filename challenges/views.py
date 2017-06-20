# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.conf import settings
from django.shortcuts import render,redirect
from challenges.models import Challenges
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from logs.models import Logs
from django.utils.encoding import smart_str
from django.http import HttpResponse

@login_required(login_url='userLogin')
def challengeDownload(request,challenge_id):
    challenge = Challenges.objects.get(id=challenge_id)
    path_to_file = os.path.join(settings.BASE_DIR, 'media',smart_str(challenge.chall_file))
    print path_to_file
    with open(path_to_file, 'rb') as fh:
        response = HttpResponse(fh.read(),content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(challenge.chall_file)
    return response

@login_required(login_url='userLogin')
def challenges(request):
    challs = Challenges.objects.all().order_by('category')
    return render(request,'challenges.html',{'challs':challs})

@login_required(login_url='userLogin')
def challengeRegister(request):
    categorys = Challenges._meta.get_field('category').choices
    if request.method == "POST":
        data = request.POST
        chall_file = request.FILES['chall_file'] if 'chall_file' in request.FILES else None
        user = User.objects.get(id=request.user.id)
        Challenges(name=data['name'],points=data['points'],description=data['description'],writeup=data['writeup'],category=data['category'],chall_file=chall_file,flag=data['flag'],created_by=user).save()
        print Logs(user_logged=request.user,function='challenges',message='Create %s challenge' % data['name']).save()
        return redirect('challenges')

    return render(request,'challenge_register.html',{'categorys':categorys})

@login_required(login_url='userLogin')
def challengeEdit(request,challenge_id):
    categorys = Challenges._meta.get_field('category').choices
    challenge = Challenges.objects.get(id=challenge_id)
    if request.user.id == challenge.created_by.id or request.user.is_staff:
        if request.method == "POST":
            data = request.POST
            user = User.objects.get(id=request.user.id)
            chall_file = request.FILES['chall_file'] if 'chall_file' in request.FILES else challenge.chall_file
            challenge.name=data['name']
            challenge.points=data['points']
            challenge.flag=data['flag']
            challenge.description=data['description']
            challenge.writeup=data['writeup']
            challenge.category=data['category']
            challenge.chall_file=chall_file
            challenge.save(update_fields=["name","points","description","writeup","category","chall_file","flag"])
            Logs(user_logged=request.user,function='challenges',message='Edit %s challenge' % data['name']).save()
            return redirect('challenges')
        return render(request,'challenge_register.html',{'categorys':categorys,'challenge':challenge})
    return redirect('challenges')

@login_required(login_url='userLogin')
def challengeDelete(request,challenge_id):
    challenge = Challenges.objects.get(id=challenge_id)
    if request.user.id == challenge.created_by.id or request.user.is_staff:
        print Logs(user_logged=request.user,function='challenges',message='Delete %s challenge' % challenge.name).save()
        challenge.delete()
    return redirect('challenges')
