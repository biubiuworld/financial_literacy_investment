from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class InvestmentInstruction(Page):
    pass

class InvestmentGame1(Page):
    form_model = 'player'
    form_fields = ['game2_slider1']

    def vars_for_template(self):
        return {
        'prob_A': self.player.prob_A_1,
        'prob_B': 1-self.player.prob_A_1,
        }
    def before_next_page(self):
        self.participant.vars['game2_slider1'] = self.player.game2_slider1

class InvestmentGame2(Page):
    form_model = 'player'
    form_fields = ['game2_slider2']
    def vars_for_template(self):
        return {
        'prob_A': self.player.prob_A_2,
        'prob_B': 1-self.player.prob_A_2,
        }
    def before_next_page(self):
        self.participant.vars['game2_slider2'] = self.player.game2_slider2

class InvestmentGame3(Page):
    form_model = 'player'
    form_fields = ['game2_slider3']
    def vars_for_template(self):
        return {
        'prob_A': self.player.prob_A_3,
        'prob_B': 1-self.player.prob_A_3,
        }
    def before_next_page(self):
        self.participant.vars['game2_slider3'] = self.player.game2_slider3

class InvestmentGame4(Page):
    form_model = 'player'
    form_fields = ['game2_slider4']

    def vars_for_template(self):
        return {
        'prob_A': self.player.prob_A_4,
        'prob_B': 1-self.player.prob_A_4,
        }
    def before_next_page(self):
        self.participant.vars['game2_slider4'] = self.player.game2_slider4

class InvestmentGame5(Page):
    form_model = 'player'
    form_fields = ['game2_slider5']

    def vars_for_template(self):
        return {
        'prob_A': self.player.prob_A_5,
        'prob_B': 1-self.player.prob_A_5,
        }
    def before_next_page(self):
        self.participant.vars['game2_slider5'] = self.player.game2_slider5

class InvestmentGame6(Page):
    form_model = 'player'
    form_fields = ['game2_slider6']

    def vars_for_template(self):
        return {
        'prob_A': self.player.prob_A_6,
        'prob_B': 1-self.player.prob_A_6,
        }
    def before_next_page(self):
        self.participant.vars['game2_slider6'] = self.player.game2_slider6

class InvestmentGame7(Page):
    form_model = 'player'
    form_fields = ['game2_slider7']

    def vars_for_template(self):
        return {
        'prob_A': round(self.player.prob_A_7, 1),
        'prob_B': round(1.-self.player.prob_A_7, 1),
        }
    def before_next_page(self):
        self.participant.vars['game2_slider7'] = self.player.game2_slider7

class InvestmentGame8(Page):
    form_model = 'player'
    form_fields = ['game2_slider8']
    def vars_for_template(self):
        return {
        'prob_A': round(self.player.prob_A_8, 1),
        'prob_B': round(1.-self.player.prob_A_8, 1),
        }
    def before_next_page(self):
        self.participant.vars['game2_slider8'] = self.player.game2_slider8

class InvestmentGame9(Page):
    form_model = 'player'
    form_fields = ['game2_slider9']
    def vars_for_template(self):
        return {
        'prob_A': round(self.player.prob_A_9, 1),
        'prob_B': round(1. - self.player.prob_A_9, 1),
        }
    def before_next_page(self):
        self.participant.vars['game2_slider9'] = self.player.game2_slider9

class InvestmentGameWaitPage(WaitPage):
    wait_for_all_groups = True





page_sequence = [InvestmentInstruction, InvestmentGame1, InvestmentGame2, InvestmentGame3, InvestmentGame4,
                 InvestmentGame5, InvestmentGame6, InvestmentGame7, InvestmentGame8, InvestmentGame9, InvestmentGameWaitPage]

