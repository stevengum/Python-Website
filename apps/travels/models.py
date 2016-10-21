from __future__ import unicode_literals
import re
from django.db import models
from ..login_reg.models import User

TRIP_REGEX = re.compile(r'^[a-zA-Z0-9\.\,\-]$')

class TripManager(models.Manager):
    def validate(self, data, pid):
        errors = []
        if len(data['destination']) < 1:
            errors.append(("You need a destination!", "destination"))
        if len(data['description']) < 1:
            errors.append(("You need a description!", "description"))
        if len(data['start_date']) < 1:
            errors.append(("You must provide a valid start date!", "start_date"))
        if len(data['end_date']) < 1:
            errors.append(("You must provide a valid end date!", "end_date"))
        if errors:
            return (False, errors)
        newtrip = self.create(planner_id=pid,destination=data['destination'],description=data['description'],start_date=data['start_date'],end_date=data['end_date'])
        return (True, newtrip)



class Trip(models.Model):
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="empty")
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    planner_id = models.ForeignKey(User, related_name="organizer")
    objects = TripManager()

class Guest(models.Model):
    trip_id = models.ManyToManyField(Trip)
    user_id = models.ManyToManyField(User)
