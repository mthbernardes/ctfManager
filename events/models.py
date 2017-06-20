# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models
from django.contrib.auth.models import User
from challenges.models import Challenges
from django import template

register = template.Library()

class Events(models.Model):
    event_tag = models.CharField(max_length=255,default=uuid.uuid4,null=True, blank=True, unique=True, editable=False)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    prize = models.TextField(null=True)
    event_wallpaper = models.FileField(upload_to='events/wallpaper',null=True)
    event_logo = models.FileField(upload_to='events/logo',null=True)
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    created_by = models.ForeignKey(User,related_name='create_event')
    status = models.BooleanField(default=False)

class EventsChallenges(models.Model):
    challenge = models.ForeignKey(Challenges,related_name='EventsChallenges_challenges')
    event = models.ForeignKey(Events,related_name='EventsChallenges_events')
