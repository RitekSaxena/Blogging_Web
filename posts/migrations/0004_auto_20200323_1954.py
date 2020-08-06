# Generated by Django 3.0.4 on 2020-03-23 14:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_pubdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='post_related',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 23, 19, 54, 6, 285527)),
        ),
    ]