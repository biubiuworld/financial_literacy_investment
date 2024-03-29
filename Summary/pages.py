from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants




class ResultsWaitPage(WaitPage):
    after_all_players_arrive = "get_payoff"


class Results(Page):
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
            'endowment_game1': self.participant.vars['endowment_game1'],
            'value_of_B_0p1_game1': self.participant.vars['value_of_B_0p1_game1'],
            'value_of_B_0p2_game1': self.participant.vars['value_of_B_0p2_game1'],
            'value_of_B_0p3_game1': self.participant.vars['value_of_B_0p3_game1'],
            'value_of_B_0p4_game1': self.participant.vars['value_of_B_0p4_game1'],
            'value_of_B_0p5_game1': self.participant.vars['value_of_B_0p5_game1'],
            'value_of_B_0p6_game1': self.participant.vars['value_of_B_0p6_game1'],
            'value_of_B_0p7_game1': self.participant.vars['value_of_B_0p7_game1'],
            'value_of_B_0p8_game1': self.participant.vars['value_of_B_0p8_game1'],
            'value_of_B_0p9_game1': self.participant.vars['value_of_B_0p9_game1'],
            'payoff_game1_p10': self.participant.vars['payoff_game1_p10'],
            'payoff_game1_p20': self.participant.vars['payoff_game1_p20'],
            'payoff_game1_p30': self.participant.vars['payoff_game1_p30'],
            'payoff_game1_p40': self.participant.vars['payoff_game1_p40'],
            'payoff_game1_p50': self.participant.vars['payoff_game1_p50'],
            'payoff_game1_p60': self.participant.vars['payoff_game1_p60'],
            'payoff_game1_p70': self.participant.vars['payoff_game1_p70'],
            'payoff_game1_p80': self.participant.vars['payoff_game1_p80'],
            'payoff_game1_p90': self.participant.vars['payoff_game1_p90'],
            'endowment_game2': self.participant.vars['endowment_game2'],
            'value_of_B_0p1_game2': self.participant.vars['value_of_B_0p1_game2'],
            'value_of_B_0p2_game2': self.participant.vars['value_of_B_0p2_game2'],
            'value_of_B_0p3_game2': self.participant.vars['value_of_B_0p3_game2'],
            'value_of_B_0p4_game2': self.participant.vars['value_of_B_0p4_game2'],
            'value_of_B_0p5_game2': self.participant.vars['value_of_B_0p5_game2'],
            'value_of_B_0p6_game2': self.participant.vars['value_of_B_0p6_game2'],
            'value_of_B_0p7_game2': self.participant.vars['value_of_B_0p7_game2'],
            'value_of_B_0p8_game2': self.participant.vars['value_of_B_0p8_game2'],
            'value_of_B_0p9_game2': self.participant.vars['value_of_B_0p9_game2'],
            'payoff_game2_p10': self.participant.vars['payoff_game2_p10'],
            'payoff_game2_p20': self.participant.vars['payoff_game2_p20'],
            'payoff_game2_p30': self.participant.vars['payoff_game2_p30'],
            'payoff_game2_p40': self.participant.vars['payoff_game2_p40'],
            'payoff_game2_p50': self.participant.vars['payoff_game2_p50'],
            'payoff_game2_p60': self.participant.vars['payoff_game2_p60'],
            'payoff_game2_p70': self.participant.vars['payoff_game2_p70'],
            'payoff_game2_p80': self.participant.vars['payoff_game2_p80'],
            'payoff_game2_p90': self.participant.vars['payoff_game2_p90'],
            'payoff1': self.participant.vars['payoff1'],
            'payoff2': self.participant.vars['payoff2'],
            'payoff3': self.participant.vars['payoff3'],
            'payoff4': self.participant.vars['payoff4'],
            'payoff5': self.participant.vars['payoff5'],
            'payoff6': self.participant.vars['payoff6'],
            'total_payoff': self.participant.vars['total_payoff'],
        }




page_sequence = [ResultsWaitPage, Results]
