# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0003_auto_20160804_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='arrival',
        ),
        migrations.RemoveField(
            model_name='package',
            name='arrival_date',
        ),
        migrations.RemoveField(
            model_name='package',
            name='arrival_time',
        ),
        migrations.RemoveField(
            model_name='package',
            name='departure',
        ),
        migrations.RemoveField(
            model_name='package',
            name='departure_date',
        ),
        migrations.RemoveField(
            model_name='package',
            name='departure_time',
        ),
    ]
