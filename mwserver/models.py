# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField('full name', max_length=32)

    def __str__(self):
        return '[' + self.name + ']'


class Measurement(models.Model):
    name = models.CharField('name as initials on fitbit', max_length=3)
    weight = models.FloatField('weight in lbs')
    date = models.DateTimeField('date taken')

    def __str__(self):
        return self.name + ':' + str(self.weight)

