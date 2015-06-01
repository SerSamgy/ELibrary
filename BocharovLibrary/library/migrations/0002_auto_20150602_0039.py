# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(to='library.Genre', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_city',
            field=models.ForeignKey(to='library.Cities', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=library.models.YearModelField(null=True),
        ),
        migrations.AlterField(
            model_name='libraryuser',
            name='birth_year',
            field=library.models.YearModelField(null=True, verbose_name='year'),
        ),
        migrations.AlterField(
            model_name='libraryuser',
            name='city',
            field=models.ForeignKey(null=True, verbose_name='city', to='library.Cities'),
        ),
    ]
