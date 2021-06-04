from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


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
        print(self.participant.vars)
        return {
            'num_of_correct_answers': self.participant.vars["num_of_correct_answers_part1"],
            'self_evaluation1': self.participant.vars['self_evaluation1'],
            'self_evaluation2': self.participant.vars['self_evaluation2'],
            'ranking': self.participant.vars['ranking']
        }


page_sequence = [Control, Treatment1, Treatment2]
