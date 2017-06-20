# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Logs(models.Model):
    function = models.CharField(max_length=255, null=False)
    message = models.CharField(max_length=255, null=False)
    user_logged = models.ForeignKey(User,related_name='user_logged')
