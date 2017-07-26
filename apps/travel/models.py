# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login.models import User
import datetime
import time
# Create your models here.
class TripManager(models.Manager):
    def addTrip(self, postData, request):
        results = {"valid": True, "errors": []}
        if not postData['destination']:
            results['errors'].append("Please give us a destination")
            results['valid'] = False
        if not postData['description']:
            results['errors'].append("Please give us a description")
            results['valid'] = False
        if not postData['start']:
            results['errors'].append("Please give us a start date")
            results['valid'] = False
        if not postData['end']:
            results['errors'].append("Please give us an end date")
            results['valid'] = False
        if postData['start'] > postData['end']:
            results['valid'] = False
            results['errors'].append('Date From must be before Date To')
        if str(datetime.datetime.today()) > postData['start']:
            results['valid'] = False
            results['errors'].append('Date From cannot be in the past')
        if results['valid']:
            startDate = datetime.datetime.strptime(postData['start'], '%Y-%m-%d')
            endDate = datetime.datetime.strptime(postData['end'], '%Y-%m-%d')
            Trip.objects.create(owner = User.objects.get(id = request.session['id']), destination = postData['destination'], start = startDate, end = endDate, plan = postData['description'])
        return results

class Trip(models.Model):
    owner = models.ForeignKey(User)
    destination = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
    plan = models.TextField(max_length=1000)
    others = models.ManyToManyField(User, related_name="others")
    date_added = models.DateTimeField(auto_now_add=True)
    objects = TripManager()
    def __str__(self):
        return str(self.start)