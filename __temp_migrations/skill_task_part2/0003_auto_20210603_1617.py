# Generated by Django 2.2.12 on 2021-06-03 23:17

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('skill_task_part2', '0002_auto_20210603_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='part2_skill_question1',
            field=otree.db.models.IntegerField(choices=[[1, 'A. Less than 2 years'], [2, 'B. Exactly $102'], [3, 'C. Less than $102']], null=True, verbose_name="\n                Suppose you owe $1000 on a loan and the interest rate you are charged is 20% per year compounded annually. \n                If you didn't pay anything off, at this interest rate, how many years would it take for the amount you \n                owe to double?\n\n                "),
        ),
    ]
