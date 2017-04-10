# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import Measurement

# Create your views here.

def index(req):
    latest_measurements = Measurement.objects.order_by('-date')[:5]
    recs = [ m.name + ':' + str(m.weight) + ' ' + m.date.strftime("[%Y %b %d]")
             for m in latest_measurements ]
    output = ', '.join(recs)
    return HttpResponse("Hello, world--this is the MW index.<br><br>"
                        + output)

def detail_user(req, id):
    return HttpResponse("Here would be some details for user %s." % id)

def detail_measurement(req, id):
    return HttpResponse("Here would be some details for measurement %s." % id)

def enter_measurement(req):
    return HttpResponse("Here you would enter a measurement.")

