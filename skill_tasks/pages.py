from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Question1(Page):
    form_model = 'player'
    form_fields = ['skill_question1', 'confidence_level_question1']


class Question2(Page):
    form_model = 'player'
    form_fields = ['skill_question2', 'confidence_level_question2']

class Question3(Page):
    form_model = 'player'
    form_fields = ['skill_question3', 'confidence_level_question3']

class Question4(Page):
    form_model = 'player'
    form_fields = ['skill_question4', 'confidence_level_question4']

class Question5(Page):
    form_model = 'player'
    form_fields = ['skill_question5', 'confidence_level_question5']

class Question6(Page):
    form_model = 'player'
    form_fields = ['skill_question6', 'confidence_level_question6']



class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Question1, Question2, Question3, Question4, Question5, Question6, Results]
