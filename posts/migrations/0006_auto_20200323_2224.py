# Generated by Django 3.0.4 on 2020-03-23 16:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200323_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 23, 22, 24, 55, 986627)),
        ),
    ]
