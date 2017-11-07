# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arbitros', '0002_auto_20171106_2350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agenda',
            old_name='Arbitro',
            new_name='arbitro',
        ),
        migrations.RenameField(
            model_name='agenda',
            old_name='Partido',
            new_name='partido',
        ),
    ]
