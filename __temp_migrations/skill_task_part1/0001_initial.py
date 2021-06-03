# Generated by Django 2.2.12 on 2021-06-03 07:21

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_task_part1_group', to='otree.Session')),
            ],
            options={
                'db_table': 'skill_task_part1_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skill_task_part1_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'skill_task_part1_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('num_of_correct_answers', otree.db.models.IntegerField(default=0, null=True)),
                ('part1_skill_question1', otree.db.models.IntegerField(choices=[[1, 'A. More than $102'], [2, 'B. Exactly $102'], [3, 'C. Less than $102']], null=True, verbose_name='\n                Suppose you have $100 in a savings account earning 2 percent interest a year. \n                After five years, how much would you have?\n                ')),
                ('part1_skill_question2', otree.db.models.IntegerField(choices=[[1, 'A. More'], [2, 'B. Same'], [3, 'C. Less']], null=True, verbose_name='\n                    Imagine that the interest rate on your savings account is 1 percent a year and inflation is 2 percent a year. \n                    After one year, would the money in the account buy more than it does today, exactly the same or less than today?\n                    ')),
                ('part1_skill_question3', otree.db.models.IntegerField(choices=[[1, 'A. True'], [2, 'B. False']], null=True, verbose_name='\n                 Buying a single company’s stock usually provides a safer return than a stock mutual fund.\n                    ')),
                ('part1_skill_question4', otree.db.models.IntegerField(choices=[[1, 'A. True'], [2, 'B. False']], null=True, verbose_name='\n        A 15-year mortgage typically requires higher monthly payments than a30-year mortgage but the total \n        interest over the life of the loan will be less.\n                        ')),
                ('part1_skill_question5', otree.db.models.IntegerField(choices=[[1, 'A. Rise'], [2, 'B. Fall'], [3, 'C. Stay the Same'], [4, 'D. No Relationship']], null=True, verbose_name='\n        If interest rates rise, what will typically happen to bond prices?  \n        Rise,fall, stay the same, or is there no relationship?\n                        ')),
                ('confidence_level_question1', otree.db.models.IntegerField(choices=[[1, '1 - Completely unconfident'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 - Completely confident']], null=True, verbose_name='How confident are you about your answer?')),
                ('confidence_level_question2', otree.db.models.IntegerField(choices=[[1, '1 - Completely unconfident'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 - Completely confident']], null=True, verbose_name='How confident are you about your answer?')),
                ('confidence_level_question3', otree.db.models.IntegerField(choices=[[1, '1 - Completely unconfident'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 - Completely confident']], null=True, verbose_name='How confident are you about your answer?')),
                ('confidence_level_question4', otree.db.models.IntegerField(choices=[[1, '1 - Completely unconfident'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 - Completely confident']], null=True, verbose_name='How confident are you about your answer?')),
                ('confidence_level_question5', otree.db.models.IntegerField(choices=[[1, '1 - Completely unconfident'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 - Completely confident']], null=True, verbose_name='How confident are you about your answer?')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='skill_task_part1.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_task_part1_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_task_part1_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skill_task_part1.Subsession')),
            ],
            options={
                'db_table': 'skill_task_part1_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skill_task_part1.Subsession'),
        ),
    ]
