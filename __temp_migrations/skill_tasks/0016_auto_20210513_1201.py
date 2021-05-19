# Generated by Django 2.2.12 on 2021-05-13 19:01

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('skill_tasks', '0015_auto_20210513_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='skill_question6',
            field=otree.db.models.IntegerField(choices=[[1, 'A. Less than 2 years'], [2, 'B. 2 to 4 years'], [3, 'C. 5 to 9 years'], [4, 'D. No Relationship']], null=True, verbose_name='\n                    Suppose you owe $1,000 on a loan and the interest rate you are charged is 20% per year \n                    compounded annually.  \n                    If you didn’t pay anything off, at this interest rate, how many years would it take for the amount \n                    you owe to double?\n                '),
        ),
    ]
