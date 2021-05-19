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


author = 'Weinan Gong'

doc = """
Step 1 Financial skill tasks (evaluating subjects' performance)
"""


class Constants(BaseConstants):
    name_in_url = 'skill_tasks'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    confidence_level_question1 = models.IntegerField(
        label="How Confident Are You about Your Answers? (out of 7)",
        min=1,
        max=7
    )
    confidence_level_question2 = models.IntegerField(
        label="How Confident Are You about Your Answers? (out of 7)",
        min=1,
        max=7
    )
    confidence_level_question3 = models.IntegerField(
        label="How Confident Are You about Your Answers? (out of 7)",
        min=1,
        max=7
    )
    confidence_level_question4 = models.IntegerField(
        label="How Confident Are You about Your Answers? (out of 7)",
        min=1,
        max=7
    )
    confidence_level_question5 = models.IntegerField(
        label="How Confident Are You about Your Answers? (out of 7)",
        min=1,
        max=7
    )
    confidence_level_question6 = models.IntegerField(
        label="How Confident Are You about Your Answers? (out of 7)",
        min=1,
        max=7
    )

    skill_question1 = models. IntegerField(
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
    skill_question2 = models.IntegerField(
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
    skill_question3 = models.IntegerField(
        label='''
                Buying a single company’s stock usually provides a safer return than a stock mutual fund.
            ''',
        choices=[
            [1, 'A. True'],
            [2, 'B. False']
        ],
        widget=widgets.RadioSelect
    )
    skill_question4 = models.IntegerField(
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
    skill_question5 = models.IntegerField(
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
        widget=widgets.RadioSelect
    )
    skill_question6 = models.IntegerField(
        label='''
                    Suppose you owe $1,000 on a loan and the interest rate you are charged is 20% per year 
                    compounded annually.  
                    If you didn’t pay anything off, at this interest rate, how many years would it take for the amount 
                    you owe to double?
                ''',
        choices=[
            [1, 'A. Less than 2 years'],
            [2, 'B. 2 to 4 years'],
            [3, 'C. 5 to 9 years'],
            [4, 'D. 10 or more years']

        ],
        widget=widgets.RadioSelect
    )

    confidence_overall1 = models.IntegerField(
        label='''
                    Among all skill questions you answered, how many questions do you think you answered correctly?
                ''',
        choices=[
            [1, 'A. Less than 2'],
            [2, 'B. 2 to 3'],
            [3, 'C. 4 to 5'],
            [4, 'D. 5 or more']

        ],
        widget=widgets.RadioSelect
    )

    confidence_overall2 = models.IntegerField(
        label='''
                        What rankings do you think you are in the all subjects?
                    ''',
        choices=[
            [1, 'A. Top 25%'],
            [2, 'B. Top 50%'],
            [3, 'C. Bottom 50%'],
            [4, 'D. Bottom 25%']

        ],
        widget=widgets.RadioSelect
    )