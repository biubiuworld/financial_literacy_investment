# Generated by Django 2.2.12 on 2021-05-13 19:15

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('skill_tasks', '0018_auto_20210513_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='confidence_level_question',
        ),
        migrations.AddField(
            model_name='player',
            name='confidence_level_question1',
            field=otree.db.models.IntegerField(choices=[[1, 'A. I Am Not Confident'], [2, 'B. I Am Somewhat Confident'], [3, 'C. I Am Confident'], [4, 'D. I Am Very Confident']], null=True, verbose_name='How Confident Are You about Your Answers?'),
        ),
        migrations.AddField(
            model_name='player',
            name='confidence_level_question2',
            field=otree.db.models.IntegerField(choices=[[1, 'A. I Am Not Confident'], [2, 'B. I Am Somewhat Confident'], [3, 'C. I Am Confident'], [4, 'D. I Am Very Confident']], null=True, verbose_name='How Confident Are You about Your Answers?'),
        ),
        migrations.AddField(
            model_name='player',
            name='confidence_level_question3',
            field=otree.db.models.IntegerField(choices=[[1, 'A. I Am Not Confident'], [2, 'B. I Am Somewhat Confident'], [3, 'C. I Am Confident'], [4, 'D. I Am Very Confident']], null=True, verbose_name='How Confident Are You about Your Answers?'),
        ),
        migrations.AddField(
            model_name='player',
            name='confidence_level_question4',
            field=otree.db.models.IntegerField(choices=[[1, 'A. I Am Not Confident'], [2, 'B. I Am Somewhat Confident'], [3, 'C. I Am Confident'], [4, 'D. I Am Very Confident']], null=True, verbose_name='How Confident Are You about Your Answers?'),
        ),
        migrations.AddField(
            model_name='player',
            name='confidence_level_question5',
            field=otree.db.models.IntegerField(choices=[[1, 'A. I Am Not Confident'], [2, 'B. I Am Somewhat Confident'], [3, 'C. I Am Confident'], [4, 'D. I Am Very Confident']], null=True, verbose_name='How Confident Are You about Your Answers?'),
        ),
        migrations.AddField(
            model_name='player',
            name='confidence_level_question6',
            field=otree.db.models.IntegerField(choices=[[1, 'A. I Am Not Confident'], [2, 'B. I Am Somewhat Confident'], [3, 'C. I Am Confident'], [4, 'D. I Am Very Confident']], null=True, verbose_name='How Confident Are You about Your Answers?'),
        ),
    ]