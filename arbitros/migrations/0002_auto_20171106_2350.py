# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arbitros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arbitro',
            name='fecha',
        ),
        migrations.AddField(
            model_name='arbitro',
            name='telefono',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
