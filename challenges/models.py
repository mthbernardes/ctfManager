# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Challenges(models.Model):
    challenges_category = (('rev', 'Reversing'),
    ('crypto', 'Cryptography'),
    ('net', 'Networing'),
    ('misc', 'Miscellaneous'),
    ('web', 'Web'),
    ('xpl', 'Exploitation'),
    ('prog','Programming'),
    ('for','Forensics'),
    ('stego','Steganography'),
    ('pwn','Pwning'))
    name = models.CharField(max_length=255, null=False)
    flag = models.CharField(max_length=255, null=False)
    points = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    writeup = models.TextField(null=True)
    chall_file = models.FileField(upload_to='challenges',null=True)
    created_by = models.ForeignKey(User,related_name='created_by_user')
    created_at = models.DateTimeField(auto_now_add=True,null=False)
    category = models.CharField(choices=challenges_category,null=False,max_length=10)
