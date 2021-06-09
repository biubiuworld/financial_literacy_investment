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
    name_in_url = 'Investment_game_part2'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    game2_slider1 = models.FloatField()
    game2_slider2 = models.FloatField()
    game2_slider3 = models.FloatField()
    game2_slider4 = models.FloatField()
    game2_slider5 = models.FloatField()
    game2_slider6 = models.FloatField()
    game2_slider7 = models.FloatField()
    game2_slider8 = models.FloatField()
    game2_slider9 = models.FloatField()


    prob_A_1 = models.FloatField(initial =.1)
    prob_A_2 = models.FloatField(initial =.2)
    prob_A_3 = models.FloatField(initial =.3)
    prob_A_4 = models.FloatField(initial =.4)
    prob_A_5 = models.FloatField(initial =.5)
    prob_A_6 = models.FloatField(initial =.6)
    prob_A_7 = models.FloatField(initial =.7)
    prob_A_8 = models.FloatField(initial =.8)
    prob_A_9 = models.FloatField(initial =.9)


