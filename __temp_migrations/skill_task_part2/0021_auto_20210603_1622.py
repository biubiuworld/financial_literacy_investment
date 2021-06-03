# Generated by Django 2.2.12 on 2021-06-03 23:22

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('skill_task_part2', '0020_auto_20210603_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='part2_skill_question4',
            field=otree.db.models.IntegerField(choices=[[1, 'A. It is a less risky investment'], [2, 'B. It can yield a higher return on investment'], [3, 'C. To have ownership in a company'], [4, 'D. The price paid when stock is sold to an investment bank']], null=True, verbose_name='\n        Why would someone buy a bond instead of a stock?\n                        '),
        ),
    ]
