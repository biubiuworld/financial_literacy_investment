# Generated by Django 2.2.12 on 2021-05-21 18:31

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('skill_task', '0002_auto_20210521_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='age',
            field=otree.db.models.IntegerField(null=True, verbose_name='1. How old are you?'),
        ),
        migrations.AddField(
            model_name='player',
            name='gender',
            field=otree.db.models.IntegerField(choices=[[0, 'Male'], [1, 'Female'], [2, 'Other'], [3, 'Prefer not to say']], null=True, verbose_name='2. What is your gender?'),
        ),
    ]
