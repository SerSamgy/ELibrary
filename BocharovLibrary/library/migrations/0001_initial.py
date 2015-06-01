# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import library.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryUser',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('login', models.CharField(unique=True, max_length=24, verbose_name='login')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='email address')),
                ('birth_year', library.models.YearModelField(verbose_name='year')),
                ('sex', models.CharField(max_length=1, default='M', verbose_name='sex')),
                ('banned', models.BooleanField(default=False, verbose_name='banned')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('author', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=255)),
                ('year', library.models.YearModelField()),
                ('publisher', models.CharField(max_length=64)),
                ('book_file', models.FileField(upload_to='books/')),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('city_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(to='library.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='pub_city',
            field=models.ForeignKey(to='library.Cities'),
        ),
        migrations.AddField(
            model_name='libraryuser',
            name='city',
            field=models.ForeignKey(to='library.Cities', verbose_name='city'),
        ),
    ]
