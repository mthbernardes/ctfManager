# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from events.models import Events,EventsChallenges
from challenges.models import Challenges

def platform(request,event_tag):
    event = Events.objects.get(event_tag=event_tag)
    challenges = Challenges.objects.all().order_by('category')
    return render(request,'platform.html',{'event':event,'challenges':challenges})
