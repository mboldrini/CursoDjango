# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170425_1435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['name'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AddField(
            model_name='course',
            name='about',
            field=models.TextField(blank=True, verbose_name='Sobre o Curso'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descricao Simples'),
        ),
    ]
