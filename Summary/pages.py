from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Summary(Page):
    def vars_for_template(self):
        return{
            'num_of_correct_answers_part1': self.participant.vars["num_of_correct_answers_part1"],
            'num_of_correct_answers_part2': self.participant.vars["num_of_correct_answers_part2"],
            'self_evaluation1': self.participant.vars['self_evaluation1'],
            'self_evaluation2': self.participant.vars['self_evaluation2'],
            'ranking': self.participant.vars['ranking'],
            'ranking_subgroup': self.participant.vars['ranking_subgroup'],
            'game1_accountA_p10': self.participant.vars['game1_slider1'],
            'game1_accountB_p10': 100-self.participant.vars['game1_slider1'],
            'game1_accountA_p20': self.participant.vars['game1_slider2'],
            'game1_accountB_p20': 100 - self.participant.vars['game1_slider2'],
            'game1_accountA_p30': self.participant.vars['game1_slider3'],
            'game1_accountB_p30': 100 - self.participant.vars['game1_slider3'],
            'game1_accountA_p40': self.participant.vars['game1_slider4'],
            'game1_accountB_p40': 100 - self.participant.vars['game1_slider4'],
            'game1_accountA_p50': self.participant.vars['game1_slider5'],
            'game1_accountB_p50': 100 - self.participant.vars['game1_slider5'],
            'game1_accountA_p60': self.participant.vars['game1_slider6'],
            'game1_accountB_p60': 100 - self.participant.vars['game1_slider6'],
            'game1_accountA_p70': self.participant.vars['game1_slider7'],
            'game1_accountB_p70': 100 - self.participant.vars['game1_slider7'],
            'game1_accountA_p80': self.participant.vars['game1_slider8'],
            'game1_accountB_p80': 100 - self.participant.vars['game1_slider8'],
            'game1_accountA_p90': self.participant.vars['game1_slider9'],
            'game1_accountB_p90': 100 - self.participant.vars['game1_slider9'],
            'game2_accountA_p10': self.participant.vars['game2_slider1'],
            'game2_accountB_p10': 100 - self.participant.vars['game2_slider1'],
            'game2_accountA_p20': self.participant.vars['game2_slider2'],
            'game2_accountB_p20': 100 - self.participant.vars['game2_slider2'],
            'game2_accountA_p30': self.participant.vars['game2_slider3'],
            'game2_accountB_p30': 100 - self.participant.vars['game2_slider3'],
            'game2_accountA_p40': self.participant.vars['game2_slider4'],
            'game2_accountB_p40': 100 - self.participant.vars['game2_slider4'],
            'game2_accountA_p50': self.participant.vars['game2_slider5'],
            'game2_accountB_p50': 100 - self.participant.vars['game2_slider5'],
            'game2_accountA_p60': self.participant.vars['game2_slider6'],
            'game2_accountB_p60': 100 - self.participant.vars['game2_slider6'],
            'game2_accountA_p70': self.participant.vars['game2_slider7'],
            'game2_accountB_p70': 100 - self.participant.vars['game2_slider7'],
            'game2_accountA_p80': self.participant.vars['game2_slider8'],
            'game2_accountB_p80': 100 - self.participant.vars['game2_slider8'],
            'game2_accountA_p90': self.participant.vars['game2_slider9'],
            'game2_accountB_p90': 100 - self.participant.vars['game2_slider9'],
        }


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Summary, ResultsWaitPage, Results]
