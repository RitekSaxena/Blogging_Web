# Generated by Django 3.0.4 on 2020-04-02 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20200402_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 22, 50, 44, 700493)),
        ),
    ]