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
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Summary'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
    # value_of_B_0p1_game1 = random.choices([3,1], weights = [1, 9])[0]
    # value_of_B_0p2_game1 = random.choices([3,1], weights = [2, 8])[0]
    # value_of_B_0p3_game1 = random.choices([3,1], weights = [3, 7])[0]
    # value_of_B_0p4_game1 = random.choices([3,1], weights = [4, 6])[0]
    # value_of_B_0p5_game1 = random.choices([3,1], weights = [5, 5])[0]
    # value_of_B_0p6_game1 = random.choices([3,1], weights = [6, 4])[0]
    # value_of_B_0p7_game1 = random.choices([3,1], weights = [7, 3])[0]
    # value_of_B_0p8_game1 = random.choices([3,1], weights = [8, 2])[0]
    # value_of_B_0p9_game1 = random.choices([3,1], weights = [9, 1])[0]

