from __future__ import unicode_literals
import uuid

from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

from drivers.models import Driver


class Package(models.Model):
    author = models.ForeignKey(User, related_name='packages')
    package_width = models.FloatField(null=True)
    package_height = models.FloatField(null=True)
    package_thickness = models.FloatField(null=True)
    package_weight = models.FloatField(null=True)
    price = models.IntegerField(null=True)
    accepted = models.BooleanField(default=False)
    phonenumber = PhoneNumberField(null=True)
    driver = models.ForeignKey(Driver, related_name='packages', blank=True,
                               null=True)
    slug = models.SlugField(default=uuid.uuid1, unique=True)
