# Generated by Django 2.2.12 on 2021-05-26 04:46

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('skill_task', '0009_auto_20210525_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='self_evaluation1',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='self_evaluation2_slider',
            field=otree.db.models.FloatField(choices=[(0, 0), (0.1, 0.1), (0.2, 0.2), (0.3, 0.3), (0.4, 0.4), (0.5, 0.5), (0.6, 0.6), (0.7, 0.7), (0.8, 0.8), (0.9, 0.9), (1, 1)], null=True),
        ),
    ]
