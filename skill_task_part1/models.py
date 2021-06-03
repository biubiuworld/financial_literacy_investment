from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'skill_task_part1'
    players_per_group = None
    num_rounds = 1
    confidence_choices = [
        [1, '1 - Completely unconfident'],
        [2, '2'],
        [3, '3'],
        [4, '4'],
        [5, '5'],
        [6, '6'],
        [7, '7 - Completely confident']
    ]
    correct_answer = [1,1,1,1,1]



class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            player.treatment_group = random.choice([0,1,2])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    num_of_correct_answers_part1 = models.IntegerField(initial =0)
    part1_skill_question1 = models.IntegerField(
        label='''
                Suppose you have $100 in a savings account earning 2 percent interest a year. 
                After five years, how much would you have?
                ''',
        choices=[
            [1, 'A. More than $102'],
            [2, 'B. Exactly $102'],
            [3, 'C. Less than $102']
        ],
        widget=widgets.RadioSelect
    )
    part1_skill_question2 = models.IntegerField(
        label='''
                    Imagine that the interest rate on your savings account is 1 percent a year and inflation is 2 percent a year. 
                    After one year, would the money in the account buy more than it does today, exactly the same or less than today?
                    ''',
        choices=[
            [1, 'A. More'],
            [2, 'B. Same'],
            [3, 'C. Less']
        ],
        widget=widgets.RadioSelect
    )
    part1_skill_question3 = models.IntegerField(
        label='''
                 Buying a single company’s stock usually provides a safer return than a stock mutual fund.
                    ''',
        choices=[
            [1, 'A. True'],
            [2, 'B. False']
        ],
        widget=widgets.RadioSelect
    )
    part1_skill_question4 = models.IntegerField(
        label='''
        A 15-year mortgage typically requires higher monthly payments than a30-year mortgage but the total 
        interest over the life of the loan will be less.
                        ''',
        choices=[
            [1, 'A. True'],
            [2, 'B. False']
        ],
        widget=widgets.RadioSelect
    )
    part1_skill_question5 = models.IntegerField(
        label='''
        If interest rates rise, what will typically happen to bond prices?  
        Rise,fall, stay the same, or is there no relationship?
                        ''',
        choices=[
            [1, 'A. Rise'],
            [2, 'B. Fall'],
            [3, 'C. Stay the Same'],
            [4, 'D. No Relationship']

        ],
        widget=widgets.RadioSelect()
    )

    confidence_level_question1 = models.IntegerField(
        label="How confident are you about your answer?",
        choices=Constants.confidence_choices,
        widget=widgets.RadioSelectHorizontal
    )

    confidence_level_question2 = models.IntegerField(
        label="How confident are you about your answer?",
        choices=Constants.confidence_choices,
        widget=widgets.RadioSelectHorizontal
    )

    confidence_level_question3 = models.IntegerField(
        label="How confident are you about your answer?",
        choices=Constants.confidence_choices,
        widget=widgets.RadioSelectHorizontal
    )

    confidence_level_question4 = models.IntegerField(
        label="How confident are you about your answer?",
        choices=Constants.confidence_choices,
        widget=widgets.RadioSelectHorizontal
    )

    confidence_level_question5 = models.IntegerField(
        label="How confident are you about your answer?",
        choices=Constants.confidence_choices,
        widget=widgets.RadioSelectHorizontal
    )

    self_evaluation1 = models.IntegerField(widget = widgets.RadioSelectHorizontal(),
        choices=
            [1,2,3,4,5],
            )
    self_evaluation2 = models.IntegerField(widget = widgets.RadioSelectHorizontal(),
        choices=
            [[10, "10%"],[20, "20%"],[30, "30%"],[40, "40%"],[50, "50%"],
             [60, "60%"],[70, "70%"],[80, "80%"],[90, "90%"],[100, "100%"]],
            )

    treatment_group = models.IntegerField()

