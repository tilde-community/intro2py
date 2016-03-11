from __future__ import unicode_literals

from django.db import models


class Activity(models.Model):
    """Simple model to log activities"""
    text = models.TextField(blank=True)
    when = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'activities'
