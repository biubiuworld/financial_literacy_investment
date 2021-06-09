# Generated by Django 2.2.12 on 2021-06-09 07:39

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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_task_part2_group', to='otree.Session')),
            ],
            options={
                'db_table': 'skill_task_part2_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skill_task_part2_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'skill_task_part2_subsession',
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
                ('num_of_correct_answers_part2', otree.db.models.IntegerField(default=0, null=True)),
                ('part2_skill_question1', otree.db.models.IntegerField(choices=[[1, 'A. Less than 2 years'], [2, 'B. 2 to 4 years'], [3, 'C. 5 to 9 years'], [4, 'D. 10 or more years']], null=True, verbose_name="\n                Suppose you owe $1000 on a loan and the interest rate you are charged is 20% per year compounded annually. \n                If you didn't pay anything off, at this interest rate, how many years would it take for the amount you \n                owe to double?\n\n                ")),
                ('part2_skill_question2', otree.db.models.IntegerField(choices=[[1, 'A. Corporate Bonds'], [2, 'B. Stocks'], [3, 'C. U.S Treasury Bond'], [4, 'D. Mutual Funds']], null=True, verbose_name='\n            Which of the following is the LEAST risky investment?\n                    ')),
                ('part2_skill_question3', otree.db.models.IntegerField(choices=[[1, 'A. The price the stock is sold for'], [2, 'B. Part of a company’s profit that is paid to owners'], [3, 'C. A capital gain'], [4, 'D. The price paid when stock is sold to an investment bank']], null=True, verbose_name='\n        What is a stock dividend? \n            ')),
                ('part2_skill_question4', otree.db.models.IntegerField(choices=[[1, 'A. It is a less risky investment'], [2, 'B. It can yield a higher return on investment'], [3, 'C. To have ownership in a company'], [4, 'D. To receive dividend payments']], null=True, verbose_name='\n        Why would someone buy a bond instead of a stock?\n                        ')),
                ('part2_skill_question5', otree.db.models.IntegerField(choices=[[1, 'A. The best month to buy the shares was February or March'], [2, 'B. The share price increased by about 50% over the year'], [3, 'C. The best month to buy the shares was September'], [4, 'D. None of the above']], null=True, verbose_name='\n        The following graph shows the price of one Rich Rock share over a 12-month period.\n        Which of the following statements is true?\n                        ')),
                ('part2_confidence_level_question1', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='How confident are you about your answer? (1 = not confident at all; 7 = completely confident)')),
                ('part2_confidence_level_question2', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='How confident are you about your answer? (1 = not confident at all; 7 = completely confident)')),
                ('part2_confidence_level_question3', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='How confident are you about your answer? (1 = not confident at all; 7 = completely confident)')),
                ('part2_confidence_level_question4', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='How confident are you about your answer? (1 = not confident at all; 7 = completely confident)')),
                ('part2_confidence_level_question5', otree.db.models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']], null=True, verbose_name='How confident are you about your answer? (1 = not confident at all; 7 = completely confident)')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='skill_task_part2.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_task_part2_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_task_part2_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skill_task_part2.Subsession')),
            ],
            options={
                'db_table': 'skill_task_part2_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skill_task_part2.Subsession'),
        ),
    ]
