# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Currency(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    USD = models.FloatField()
    PLN = models.FloatField()
    EUR = models.FloatField()
    CZK = models.FloatField()
    
    def __unicode__(self):
        return self.name

    class Meta():
        get_latest_by = "timestamp"


