# Generated by Django 2.2.12 on 2021-06-03 23:19

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('skill_task_part2', '0008_auto_20210603_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='part2_skill_question2',
            field=otree.db.models.IntegerField(choices=[[1, 'A. Corporate Bonds'], [2, 'B. Stocks'], [3, 'C. Less']], null=True, verbose_name='\n            Which of the following is the LEAST risky investment?\n                    '),
        ),
    ]
