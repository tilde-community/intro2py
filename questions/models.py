from __future__ import unicode_literals

from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=256)


class Question(models.Model):
    body = models.TextField()
    category = models.ForeignKey(Topic, related_name='questions')
