# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Measurement

# Create your views here.

def index(req):
    latest_measurements = Measurement.objects.order_by('-date')[:20]
    context = { 'latest_measurements' : latest_measurements }
    return render(req, 'mwserver/index.html', context)

def detail_user(req, id):
    return HttpResponse("Here would be some details for user %s." % id)

def detail_measurement(req, id):
    measurement = get_object_or_404(Measurement, pk=id)
    context = { 'm' : measurement }
    return render(req, 'mwserver/m/detail_measurement.html', context)

def enter_measurement(req):
    context = {}
    return render(req, 'mwserver/m/enter_measurement.html', context)

def post_measurement(req):
    try:
        Measurement.objects.create(name = req.POST['name'],
                                   weight = req.POST['weight'],
                                   date = req.POST['datetime'])
    except Exception as e:
        return HttpResponse("Problem entering weight.\n({}) {}".
                            format(type(e), e.message))
    else:
        return HttpResponseRedirect(reverse('mwserver:index'))
    
def report_lametric(req):
    dummy = """
{
  "frames": [
    {
      "text": "MHX LBS",
      "icon": "a343"
    },
    {
      "text": "15.8 LBS",
      "icon": null
    }
  ]
}
"""
    return HttpResponse(dummy)
