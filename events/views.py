# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render,redirect
from events.models import Events,EventsChallenges
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from logs.models import Logs
from challenges.models import Challenges
from django.utils.encoding import smart_str
from django.http import HttpResponse
from django.utils.timezone import now
from django.utils.dateparse import parse_datetime


@login_required(login_url='userLogin')
def eventChallengesAdd(request,event_id,challenge_id):
    if request.user.is_staff:
        challenge = Challenges.objects.get(id=challenge_id)
        event = Events.objects.get(id=event_id)
        EventsChallenges.objects.get_or_create(event=event,challenge=challenge)
        print Logs(user_logged=request.user,function='events',message='add %s challenge on %s Event' % (challenge.name,event.name)).save()

    return redirect('eventChallenges',event_id)

@login_required(login_url='userLogin')
def eventChallengesDel(request,event_id,challenge_id):
    if request.user.is_staff:
        challenge = Challenges.objects.get(id=challenge_id)
        event = Events.objects.get(id=event_id)
        EventsChallenges.objects.get(event=event,challenge=challenge).delete()
        print Logs(user_logged=request.user,function='events',message='del %s challenge on %s Event' % (challenge.name,event.name)).save()
    return redirect('eventChallenges',event_id)

@login_required(login_url='userLogin')
def eventChallenges(request,event_id):
    event = Events.objects.get(id=event_id)
    challenges = Challenges.objects.all().order_by('category')
    return render(request,'eventChallenges.html',{'challenges':challenges,'event':event})

@login_required(login_url='userLogin')
def events(request):
    events = Events.objects.all()
    return render(request,'events.html',{'events':events})

@login_required(login_url='userLogin')
def eventRegister(request):
    if request.user.is_staff:
        if request.method == "POST":
            event_logo = request.FILES['event_logo'] if 'event_logo' in request.FILES else None
            event_wallpaper = request.FILES['event_wallpaper'] if 'event_wallpaper' in request.FILES else None
            data = request.POST
            user = User.objects.get(id=request.user.id)
            Events(name=data['name'],
            description=data['description'],
            prize=data['prize'],
            start_date=parse_datetime(data['start_date']),
            event_wallpaper=event_wallpaper,
            event_logo=event_logo,
            end_date=parse_datetime(data['end_date']),
            created_by=user).save()
            print Logs(user_logged=request.user,function='events',message='Create %s Event' % data['name']).save()
            return redirect('events')
    else:
            return redirect('events')
    return render(request,'eventRegister.html')

@login_required(login_url='userLogin')
def eventEdit(request,event_id):
    event = Events.objects.get(id=event_id)
    if request.user.is_staff:
        if request.method == "POST":
            event_logo = request.FILES['event_logo'] if 'event_logo' in request.FILES else event.event_logo
            event_wallpaper = request.FILES['event_wallpaper'] if 'event_wallpaper' in request.FILES else event.event_wallpaper
            data = request.POST
            event.name=data['name']
            event.description=data['description']
            event.prize=data['prize']
            event.start_date=parse_datetime(data['start_date'])
            event.end_date=parse_datetime(data['end_date'])
            event.event_wallpaper = event_wallpaper
            event.event_logo=event_logo
            event.save(update_fields=["name","description","prize","start_date","end_date","event_logo","event_wallpaper"])
            Logs(user_logged=request.user,function='events',message='Edit %s event' % data['name']).save()
            return redirect('events')
        return render(request,'eventRegister.html',{'event':event})
    return redirect('events')

@login_required(login_url='userLogin')
def eventDelete(request,event_id):
    event = Events.objects.get(id=event_id)
    if request.user.is_staff:
        print Logs(user_logged=request.user,function='events',message='Delete %s event' % event.name).save()
        event.delete()
    return redirect('events')
