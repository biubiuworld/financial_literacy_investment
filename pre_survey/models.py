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
    def agg_gender(self):
        male_count = 0
        female_count = 0
        other_count = 0
        dna_count = 0
        ## aggregate gender data
        for player in self.get_players():
            if player.gender == 0:
                male_count += 1
            elif player.gender == 1:
                female_count += 1
            elif player.gender == 2:
                other_count += 1
            elif player.gender == 3:
                dna_count += 1
        ## set gender counts
        for player in self.get_players():
            player.male_count = male_count
            player.female_count = female_count
            player.other_count = other_count
            player.dna_count = dna_count


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

    male_count = models.IntegerField(initial =0)
    female_count = models.IntegerField(initial =0)
    other_count = models.IntegerField(initial =0)
    dna_count = models.IntegerField(initial =0)
