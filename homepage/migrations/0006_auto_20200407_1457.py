# Generated by Django 3.0.4 on 2020-04-07 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20200407_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='height',
            new_name='weight',
        ),
    ]
