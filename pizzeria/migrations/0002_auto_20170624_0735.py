# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 23:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
                ('datt_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.TextField(max_length=20),
        ),
        migrations.AddField(
            model_name='topping',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzeria.Pizza'),
        ),
    ]
