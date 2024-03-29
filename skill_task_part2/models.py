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
from scipy.stats import percentileofscore
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'skill_task_part2'
    players_per_group = None
    num_rounds = 1
    confidence_choices = [
        [1, '1'],
        [2, '2'],
        [3, '3'],
        [4, '4'],
        [5, '5'],
        [6, '6'],
        [7, '7']
    ]
    correct_answer = [2, 3, 2, 1, 3]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def get_ranking(self):
        all_scores_1 = [] # stores the scores of all players
        all_scores_2 = []
        all_scores_3 = []
        all_scores_4 = []
        all_scores_5 = []
        for p in self.get_players():
            if p.participant.vars['subgroup'] == 1:
                all_scores_1.append(p.num_of_correct_answers_part2)# storing the data
            elif p.participant.vars['subgroup'] == 2:
                all_scores_2.append(p.num_of_correct_answers_part2)# storing the data
            elif p.participant.vars['subgroup'] == 3:
                all_scores_3.append(p.num_of_correct_answers_part2)# storing the data
            elif p.participant.vars['subgroup'] == 4:
                all_scores_4.append(p.num_of_correct_answers_part2)# storing the data
            else:
                all_scores_5.append(p.num_of_correct_answers_part2)  # storing the data
            print(f'skill test 2 score list is {all_scores_1}, {all_scores_2}, {all_scores_3}, {all_scores_4}, {all_scores_5}')

        # calculating the ranking of each subgroup
        for p in self.get_players():
            if p.participant.vars['subgroup'] == 1:
                p.participant.vars["ranking_subgroup"] = percentileofscore(all_scores_1, p.num_of_correct_answers_part2, "strict")
            elif p.participant.vars['subgroup'] == 2:
                p.participant.vars["ranking_subgroup"] = percentileofscore(all_scores_2, p.num_of_correct_answers_part2, "strict")
            elif p.participant.vars['subgroup'] == 3:
                p.participant.vars["ranking_subgroup"] = percentileofscore(all_scores_3, p.num_of_correct_answers_part2, "strict")
            elif p.participant.vars['subgroup'] == 4:
                p.participant.vars["ranking_subgroup"] = percentileofscore(all_scores_4, p.num_of_correct_answers_part2, "strict")
            else:
                p.participant.vars["ranking_subgroup"] = percentileofscore(all_scores_5, p.num_of_correct_answers_part2, "strict")
            print(f'skill test 2 ranking is {p.participant.vars["ranking_subgroup"]}')

class Player(BasePlayer):
    num_of_correct_answers_part2 = models.IntegerField(initial=0)
    part2_skill_question1 = models.IntegerField(
        label='''
                Suppose you owe $1000 on a loan and the interest rate you are charged is 20% per year compounded annually. 
                If you didn't pay anything off, at this interest rate, how many years would it take for the amount you 
                owe to double?

                ''',
        choices=[
            [1, 'A. Less than 2 years'],
            [2, 'B. 2 to 4 years'],
            [3, 'C. 5 to 9 years'],
            [4, 'D. 10 or more years']
        ],
        widget=widgets.RadioSelect
    )
    part2_skill_question2 = models.IntegerField(
        label='''
            Which of the following is the LEAST risky investment?
                    ''',
        choices=[
            [1, 'A. Corporate Bonds'],
            [2, 'B. Stocks'],
            [3, 'C. U.S Treasury Bond'],
            [4, 'D. Mutual Funds']
        ],
        widget=widgets.RadioSelect
    )
    part2_skill_question3 = models.IntegerField(
        label='''
        What is a stock dividend? 
            ''',
        choices=[
            [1, 'A. The price the stock is sold for'],
            [2, 'B. Part of a company’s profit that is paid to owners'],
            [3, 'C. A capital gain'],
            [4, 'D. The price paid when stock is sold to an investment bank']
        ],
        widget=widgets.RadioSelect
    )
    part2_skill_question4 = models.IntegerField(
        label='''
        Why would someone buy a bond instead of a stock?
                        ''',
        choices=[
            [1, 'A. It is a less risky investment'],
            [2, 'B. It can yield a higher return on investment'],
            [3, 'C. To have ownership in a company'],
            [4, 'D. To receive dividend payments']
        ],
        widget=widgets.RadioSelect
    )
    part2_skill_question5 = models.IntegerField(
        label='''
        The following graph shows the price of one Rich Rock share over a 12-month period.
        Which of the following statements is true?
                        ''',
        choices=[
            [1, 'A. The best month to buy the shares was February or March'],
            [2, 'B. The share price increased by about 50% over the year'],
            [3, 'C. The best month to buy the shares was September'],
            [4, 'D. None of the above']

        ],
        widget=widgets.RadioSelect()
    )

    part2_confidence_level_question1 = models.IntegerField(
        label="How confident are you about your answer? (1 = not confident at all; 7 = completely confident)",
        choices=Constants.confidence_choices,
        widget=widgets.RadioSelectHorizontal
    )

    part2_confidence_level_question2 = models.IntegerField(
        label="How confident are you about your answer? (1 = not confident at all; 7 = completely confident)",
        choices=Constants.confidence_choices,
        widget=widgets.RadioSelectHorizontal
    )

    part2_confidence_level_question3 = models.IntegerField(
        label="How confident are you about your answer? (1 = not confident at all; 7 = completely confident)",
        choices=Constants.confidence_choices,
        widget=widgets.RadioSelectHorizontal
    )

    part2_confidence_level_question4 = models.IntegerField(
        label="How confident are you about your answer? (1 = not confident at all; 7 = completely confident)",
        choices=Constants.confidence_choices,
        widget=widgets.RadioSelectHorizontal
    )

    part2_confidence_level_question5 = models.IntegerField(
        label="How confident are you about your answer? (1 = not confident at all; 7 = completely confident)",
        choices=Constants.confidence_choices,
        widget=widgets.RadioSelectHorizontal
    )
