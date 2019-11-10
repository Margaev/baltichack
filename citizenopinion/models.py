# -*- coding:utf-8 -*-
from django.utils import timezone
from django.conf import settings
from django.db import models
import datetime


class Post(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    city = models.CharField(max_length = 32)
    image = models.ImageField(upload_to = './', null = True)

    def __str__(self):
        return self.title


class Poll(models.Model):
    question = models.CharField(max_length=200)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    def __str__(self):              # Python 3: def __unicode__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):              # Python 3: def __unicode__(self):
        return self.choice_text
