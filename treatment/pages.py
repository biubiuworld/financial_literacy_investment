from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from random import choice


class Control(Page):
    def is_displayed(self):
        if self.player.treatment_group == 0:
            return True
        else:
            return False
    def vars_for_template(self):
        return {
            'self_evaluation1': self.participant.vars['self_evaluation1']
        }

class Treatment1(Page):
    def is_displayed(self):
        if self.player.treatment_group == 1:
            return True
        else:
            return False

    def vars_for_template(self):
        return {
            'num_of_correct_answers': self.participant.vars['num_of_correct_answers_part1'],
            'self_evaluation1': self.participant.vars['self_evaluation1']
        }


class Treatment2(Page):
    def is_displayed(self):
        if self.player.treatment_group == 2:
            return True
        else:
            return False

    def vars_for_template(self):

        # telling the player if he is on the top/bottom 50%
        ranking_over_50 = None
        if self.participant.vars['ranking'] >= 50:
            ranking_over_50 = "better than 50%"
        else:
            ranking_over_50 = "lower than 50%"
        return {
            'num_of_correct_answers': self.participant.vars["num_of_correct_answers_part1"],
            'self_evaluation1': self.participant.vars['self_evaluation1'],
            'self_evaluation2': self.participant.vars['self_evaluation2'],
            'ranking': ranking_over_50
        }


page_sequence = [Control, Treatment1, Treatment2]
