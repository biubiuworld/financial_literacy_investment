from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Demographics(Page):
    form_model = 'player'
    form_fields = ['ethnicity', 'race', 'education', 'major']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Demographics]
