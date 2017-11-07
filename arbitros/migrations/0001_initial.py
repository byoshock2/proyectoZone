# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Arbitro',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=60)),
                ('fecha', models.CharField(max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='agenda',
            name='Arbitro',
            field=models.ForeignKey(to='arbitros.Arbitro'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='Partido',
            field=models.ForeignKey(to='arbitros.Partido'),
        ),
    ]
