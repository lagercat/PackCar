# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0004_auto_20190408_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
