from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    pass

class Presurvey(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']


class PreSurveyWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'agg_gender'


class PreSurveyResult(Page):

    def vars_for_template(self):
        return {
            'male_count': self.player.male_count,
            'female_count': self.player.female_count,
            'other_count': self.player.other_count,
            'dna_count': self.player.dna_count
        }


page_sequence = [Introduction, Presurvey, PreSurveyWaitPage, PreSurveyResult]
