# Generated by Django 3.2.7 on 2021-09-19 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_auto_20210919_1143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='subtitile',
            new_name='subtitle',
        ),
    ]