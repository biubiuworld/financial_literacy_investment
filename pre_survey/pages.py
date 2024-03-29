from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from statistics import median

class Introduction(Page):
    pass

class Compensation(Page):
    pass

class Presurvey(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']


class PreSurveyWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'agg_gender'


class PreSurveyResult(Page):

    def vars_for_template(self):

        # calculating the median
        ages = [] # list for storing all the ages
        for p in self.group.get_players():
            ages.append(p.age)

        return {
            'male_count': self.player.male_count,
            'female_count': self.player.female_count,
            'other_count': self.player.other_count,
            'dna_count': self.player.dna_count,
            'age_median': median(ages),
            "num_demo_participants":self.session.config["num_demo_participants"],
        }


page_sequence = [Introduction, Compensation, Presurvey, PreSurveyWaitPage, PreSurveyResult]
