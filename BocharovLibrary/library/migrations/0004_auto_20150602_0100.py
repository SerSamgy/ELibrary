# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('library', '0003_auto_20150602_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='libraryuser',
            name='groups',
            field=models.ManyToManyField(related_name='user_set', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, to='auth.Group', related_query_name='user'),
        ),
        migrations.AddField(
            model_name='libraryuser',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.'),
        ),
        migrations.AddField(
            model_name='libraryuser',
            name='user_permissions',
            field=models.ManyToManyField(related_name='user_set', verbose_name='user permissions', help_text='Specific permissions for this user.', blank=True, to='auth.Permission', related_query_name='user'),
        ),
    ]
