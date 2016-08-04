from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField


class Driver(models.Model):
    departure = models.CharField(null=True, max_length=300)
    arrival = models.CharField(null=True, max_length=300)
    departure_date = models.DateField(null=True)
    departure_time = models.TimeField(null=True)
    arrival_date = models.DateField(null=True)
    arrival_time = models.TimeField(null=True)
    phonenumber = PhoneNumberField(null=True)
    author = models.ForeignKey(User, related_name='drivers')
