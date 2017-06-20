# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from logs.models import Logs
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required(redirect_field_name='dashboard',login_url='dashboard')
def logs(request):
    challenges = Logs.objects.filter(function='challenges')
    users = Logs.objects.filter(function='users')
    events = Logs.objects.filter(function='events')
    return render(request,'logs.html',{'challenges':challenges,'users':users,'events':events})
