from __future__ import unicode_literals

from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=256)


class Question(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    intro = models.TextField(null=True, blank=True)
    body = models.TextField()
    success_message = models.TextField(null=True, blank=True)
    fail_message = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Topic, related_name='questions')
