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
    name_in_url = 'skill_task'
    players_per_group = None
    num_rounds = 10 # number of skill questions

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
        ''', #q6
        '''
        Which of the following is the LEAST risky investment?
        ''' , # q7
        '''
        What is a stock dividend?
        ''' ,# q8
        '''
        Why would someone buy a bond instead of a stock?
        ''', # q9
        '''
        The following graph shows the price of one Rich Rock share over a 12-month period.
        Which statement about the graph is true?
        ''', # q10
                    ]

    skill_question_choices = [
                        [[1, 'A. More than $102'], [2, 'B. Exactly $102'], [3, 'C. Less than $102']],#q1
                        [[1, 'A. More'], [2, 'B. Same'], [3, 'C. Less']],#q2
                        [[1, 'A. True'], [2, 'B. False']],#q3
                        [[1, 'A. True'], [2, 'B. False']],#q4
                        [[1, 'A. Rise'], [2, 'B. Fall'], [3, 'C. Stay the Same'], [4, 'D. No Relationship']],#q5
                        [[1, 'A. Less than 2 years'], [2, 'B. 2 to 4 years'],
                         [3, 'C. 5 to 9 years'], [4, 'D. 10 or more years']],#q6
                        [[1, 'A. Corporate Bonds'], [2, 'B. Stocks'], [3, 'C. U.S Treasury Bond'], [4, 'D. Mutual Funds']], #q7
                        [[1, 'A. The price the stock is sold for'],
                         [2, 'B. Part of a company’s profit that is paid to owners'],
                         [3, 'C. A capital gain'], [4, 'D. The price paid when stock is sold to an investment bank']], #q8
                        [[1, 'A. It is a less risky investment'], [2, 'B. It can yield a higher return on investment'],
                         [3, 'C. To have ownership in a company'], [4, 'D. To receive dividend payments']],#q9
                        [[1, 'A. The best month to buy the shares was February or March'],
                         [2, 'B. The share price increased by about 50% over the year'],
                         [3, 'C. The best month to buy the shares was September'], [4, 'D. None of the above']]#q10
                        ]

    correct_answers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    payment_per_correct_answer = 1

class Subsession(BaseSubsession):
    def agg_gender(self):
        male_count = 0
        female_count = 0
        other_count = 0 
        dna_count = 0 
        ## aggregate gender data
        for player in self.get_players():
            if player.gender == 0:
                male_count +=1
            elif player.gender == 1:
                female_count += 1
            elif player.gender == 2:
                other_count += 1
            elif player.gender == 3:
                dna_count += 1
        ## set gender counts
        for player in self.get_players():
            player.male_count = male_count
            player.female_count = female_count
            player.other_count = other_count
            player.dna_count = dna_count




class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ## stores aggregated gender data for all players
    male_count = models.IntegerField(initial =0)
    female_count = models.IntegerField(initial =0)
    other_count = models.IntegerField(initial =0)
    dna_count = models.IntegerField(initial =0)
    # pre_survey
    age = models.IntegerField(
        min=18,
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
    confidence = models.IntegerField(widget = widgets.RadioSelectHorizontal(),
        choices=
            [1,2,3,4,5,6,7],
            )


    # Assign treatments
    treatment_group = models.IntegerField()

    def creating_treatment(subsession):
        for player in subsession.get_players():
            player.treatment_group = random.choice([0, 1, 2])


