from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'pre_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(
        min=14,
        max=100,
        label="1. How old are you?"
    )

    gender = models.IntegerField(
        label="2. What is your gender?",
        choices=[
            [0, "Male"],
            [1, "Female"],
            [2, "Other"],
            [3, "Prefer not to say"]
        ],
        widget=widgets.RadioSelect
    )
