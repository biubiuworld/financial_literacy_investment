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
    name_in_url = 'demographics_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ethnicity = models.IntegerField(
        label="1. Are you of Hispanic, Latino, or Spanish origin?",
        choices=[
            [1, 'Yes'],
            [0, 'No']
        ],
        widget=widgets.RadioSelect
    )
    race = models.IntegerField(
        choices=[
            [0, 'American Indian or Alaska Native'],
            [1, 'Asian'],
            [2, 'Black or African American'],
            [3, 'Native Hawaiian or Other Pacific Islander'],
            [4, 'White or Caucasian'],
            [5, 'Middle Eastern'],
            [6, 'Hispanic, Latino, or Spanish'],
            [7, 'Other']
        ],
        widget=widgets.RadioSelect,
        label="2. How would you best describe yourself?"
    )
    education = models.IntegerField(
        choices=[
            [1, 'Freshman'],
            [2, 'Sophomore'],
            [3, 'Junior'],
            [4, 'Senior'],
            [5, 'Graduate (Master Degree)'],
            [6, 'Graduate (Doctoral Degree)']
        ],
        widget=widgets.RadioSelect,
        label="3. What year are you in UCSC?"
    )

    major = models.StringField(
        label="4. What is your major?"
    )


