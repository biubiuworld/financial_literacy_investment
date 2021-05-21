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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'skill_task'
    players_per_group = None
    num_rounds = 6 # number of skill questions

    skill_question_text = [
        '''
        Suppose you have $100 in a savings account earning 2 percent interest a year. 
        After five years, how much would you have?
        ''', #q1
        '''
        Imagine that the interest rate on your savings account is 1 percent a year and inflation is 2 percent a year. 
        After one year, would the money in the account buy more than it does today, exactly the same or less than today?
        ''', #q2
        '''
        Buying a single company’s stock usually provides a safer return than a stock mutual fund.
        ''', #q3
        '''
        A 15-year mortgage typically requires higher monthly payments than a30-year mortgage but the total 
        interest over the life of the loan will be less.
        ''', #q4
        '''
        If interest rates rise, what will typically happen to bond prices?  
        Rise,fall, stay the same, or is there no relationship?
        ''', #q5
        '''
        Suppose you owe $1,000 on a loan and the interest rate you are charged is 20% per year compounded annually.  
        If you didn’t pay anything off, at this interest rate, how many years would it take for the amount you owe to double?
        ''' #q6
                    ]

    skill_question_choices = [
                        [[1, 'A. More than $102'], [2, 'B. Exactly $102'], [3, 'C. Less than $102']],
                        [[1, 'A. More'], [2, 'B. Same'], [3, 'C. Less']],
                        [[1, 'A. True'], [2, 'B. False']],
                        [[1, 'A. True'], [2, 'B. False']],
                        [[1, 'A. Rise'], [2, 'B. Fall'], [3, 'C. Stay the Same'], [4, 'D. No Relationship']],
                        [[1, 'A. Less than 2 years'], [2, 'B. 2 to 4 years'], [3, 'C. 5 to 9 years'], [4, 'D. 10 or more years']]
                        ]

    correct_answers = [1, 1, 1, 1, 1, 1]

    payment_per_correct_answer = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # pre_survey
    age = models.IntegerField(
        min=14,
        max=100,
        label="1. How old are you?"
    )

    gender = models.IntegerField(
        label="2. What is your gender?",
        choices=[
            [0, "Male"],
            [1, "Female"],
            [2, "Other"],
            [3, "Prefer not to say"]
        ],
        widget=widgets.RadioSelect
    )
    # Skill_tasks
    answer = models.IntegerField(widget=widgets.RadioSelect())


