# Generated by Django 3.2.7 on 2021-09-19 06:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='subtitile',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
