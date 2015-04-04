# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20150403_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='capacity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='size_limit',
            field=models.IntegerField(null=True),
        ),
    ]
