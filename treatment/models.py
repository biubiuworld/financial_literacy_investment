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
    name_in_url = 'treatment'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):

        # obtaining the ids
        player_ids = [p for p in range(1, self.session.config["num_demo_participants"] + 1)]
        random.shuffle(player_ids) # randomizing ids

        # assigning treatments randomly
        for p in self.get_players():
            if player_ids.index(p.id_in_group) <= 3:
                p.treatment_group = 0
            elif player_ids.index(p.id_in_group) <= 7:
                p.treatment_group = 1
            else:
                p.treatment_group = 2
        # # assigning treatments randomly with 4 persons
        # for p in self.get_players():
        #     if player_ids.index(p.id_in_group) <= 1:
        #         p.treatment_group = 0
        #     elif player_ids.index(p.id_in_group) <= 2:
        #         p.treatment_group = 1
        #     else:
        #         p.treatment_group = 2

        player_ids2 = [p for p in range(1, self.session.config["num_demo_participants"] + 1)]
        random.shuffle(player_ids2)
        for p in self.get_players():
            if player_ids2.index(p.id_in_group) <= 3:
                p.subgroup = 1
            elif player_ids2.index(p.id_in_group) <= 7:
                p.subgroup = 2
            elif player_ids2.index(p.id_in_group) <= 11:
                p.subgroup = 3
            elif player_ids2.index(p.id_in_group) <= 15:
                p.subgroup = 4
            else:
                p.subgroup = 5
        for p in self.get_players():
            p.participant.vars['subgroup'] = p.subgroup

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment_group = models.IntegerField()
    subgroup = models.IntegerField()
