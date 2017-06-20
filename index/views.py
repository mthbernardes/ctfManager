# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from challenges.models import Challenges
from events.models import Events,EventsChallenges
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.db.models import Count
from django.conf import settings
import requests

@login_required(login_url='userLogin')
def dashboard(request):
    try:
        ctfteam = requests.get('https://ctftime.org/api/v1/teams/%s/' % settings.TEAM_CTFTIME_ID,timeout=3).json()['rating'][0]
    except:
        ctfteam = None
    try:
        upcomming_events = requests.get('https://ctftime.org/api/v1/events/?limit=5',timeout=3).json()
    except:
        upcomming_events = None
    users = User.objects.all().annotate(num_submissions=Count('created_by_user')).order_by('num_submissions').reverse()
    challenges = Challenges.objects.all()
    events = Events.objects.all()
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    return render(request,'dashboard.html',{'users':users,'challenges':challenges,'sessions':sessions,'ctfteam':ctfteam,'upcomming_events':upcomming_events,'events':events})
