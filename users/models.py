# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import auth
from challenges.models import Challenges

@property
def total_challenges(self,):
    total = Challenges.objects.filter(created_by=self.id).count()
    print total
    return total

auth.models.User.add_to_class('total_challenges', total_challenges)
