from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class InvestmentInstruction(Page):
    pass

class InvestmentGame1(Page):
    form_model = 'player'
    form_fields = ['game1_slider1']

    def vars_for_template(self):
        return {
        # 'account_A': self.player.allocation1_a1,
        'prob_A': self.player.prob_A_1,
        'prob_B': 1-self.player.prob_A_1,
        }

class InvestmentGame2(Page):
    form_model = 'player'
    form_fields = ['game1_slider2']
    def vars_for_template(self):
        return {
        'account_A': self.player.allocation1_a2,
        'prob_A': self.player.prob_A_2,
        'prob_B': 1-self.player.prob_A_2,
        }

class InvestmentGame3(Page):
    form_model = 'player'
    form_fields = ['game1_slider3']
    def vars_for_template(self):
        return {
        'account_A': self.player.allocation1_a3,
        'prob_A': self.player.prob_A_3,
        'prob_B': 1-self.player.prob_A_3,
        }

class InvestmentGame4(Page):
    form_model = 'player'
    form_fields = ['game1_slider4']

    def vars_for_template(self):
        return {
        'account_A': self.player.allocation1_a4,
        'prob_A': self.player.prob_A_4,
        'prob_B': 1-self.player.prob_A_4,
        }

class InvestmentGame5(Page):
    form_model = 'player'
    form_fields = ['game_slider5']

    def vars_for_template(self):
        return {
        'account_A': self.player.allocation1_a5,
        'prob_A': self.player.prob_A_5,
        'prob_B': 1-self.player.prob_A_5,
        }

class InvestmentGame6(Page):
    form_model = 'player'
    form_fields = ['game1_slider6']

    def vars_for_template(self):
        return {
        'account_A': self.player.allocation1_a6,
        'prob_A': self.player.prob_A_6,
        'prob_B': 1-self.player.prob_A_6,
        }

class InvestmentGame7(Page):
    form_model = 'player'
    form_fields = ['game1_slider7']

    def vars_for_template(self):
        return {
        'account_A': self.player.allocation1_a7,
        'prob_A': self.player.prob_A_7,
        'prob_B': 1-self.player.prob_A_7,
        }

class InvestmentGame8(Page):
    form_model = 'player'
    form_fields = ['game1_slider8']
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False
    def vars_for_template(self):
        return {
        'account_A': self.player.allocation1_a8,
        'prob_A': self.player.prob_A_8,
        'prob_B': 1-self.player.prob_A_8,
        }

class InvestmentGame9(Page):
    form_model = 'player'
    form_fields = ['game1_slider9']
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False
    def vars_for_template(self):
        return {
        'account_A': self.player.allocation1_a9,
        'prob_A': self.player.prob_A_9,
        'prob_B': 1-self.player.prob_A_9,
        }

class InvestmentGameWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'set_Allocations'




page_sequence = [InvestmentInstruction, InvestmentGame1, InvestmentGame2, InvestmentGame3, InvestmentGame4,
                 InvestmentGame5, InvestmentGame6, InvestmentGame7, InvestmentGame8, InvestmentGame9, InvestmentGameWaitPage]
