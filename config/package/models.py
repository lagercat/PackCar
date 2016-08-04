from __future__ import unicode_literals
import uuid

from django.db import models
from django.contrib.auth.models import User


class Package(models.Model):
    title = models.CharField(null=True, max_length=30)
    details = models.CharField(null=True, max_length=300)
    departure = models.CharField(null=True, max_length=300)
    arrival = models.CharField(null=True, max_length=300)
    departure_date = models.DateField(null=True)
    arrival_date = models.DateField(null=True)
    author = models.ForeignKey(User, related_name='packages')
    package_width = models.FloatField(null=True)
    package_height = models.FloatField(null=True)
    package_thickness = models.FloatField(null=True)
    package_weight = models.FloatField(null=True)
    price = models.IntegerField(null=True)
    slug = models.SlugField(default=uuid.uuid1, unique=True)
