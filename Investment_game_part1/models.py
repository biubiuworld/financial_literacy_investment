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
    name_in_url = 'Investment_game_part1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    game1_slider1 = models.FloatField(widget=widgets.RadioSelectHorizontal(),
                                     choices=
                                     [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1],
                                     )
    game1_slider2 = models.FloatField(widget=widgets.RadioSelectHorizontal(),
                                     choices=
                                     [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1],
                                     )
    game1_slider3 = models.FloatField(widget=widgets.RadioSelectHorizontal(),
                                     choices=
                                     [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1],
                                     )
    game1_slider4 = models.FloatField(widget=widgets.RadioSelectHorizontal(),
                                     choices=
                                     [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1],
                                     )
    game1_slider5 = models.FloatField(widget=widgets.RadioSelectHorizontal(),
                                     choices=
                                     [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1],
                                     )
    game1_slider6 = models.FloatField(widget=widgets.RadioSelectHorizontal(),
                                     choices=
                                     [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1],
                                     )
    game1_slider7 = models.FloatField(widget=widgets.RadioSelectHorizontal(),
                                     choices=
                                     [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1],
                                     )
    game1_slider8 = models.FloatField(widget=widgets.RadioSelectHorizontal(),
                                     choices=
                                     [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1],
                                     )
    game1_slider9 = models.FloatField(widget=widgets.RadioSelectHorizontal(),
                                     choices=
                                     [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1],
                                     )

    allocation1_a1 = models.FloatField()
    allocation1_b1 = models.FloatField()
    allocation1_a2 = models.FloatField()
    allocation1_b2 = models.FloatField()
    allocation1_a3 = models.FloatField()
    allocation1_b3 = models.FloatField()
    allocation1_a4 = models.FloatField()
    allocation1_b4 = models.FloatField()
    allocation1_a5 = models.FloatField()
    allocation1_b5 = models.FloatField()
    allocation1_a6 = models.FloatField()
    allocation1_b6 = models.FloatField()
    allocation1_a7 = models.FloatField()
    allocation1_b7 = models.FloatField()
    allocation1_a8 = models.FloatField()
    allocation1_b8 = models.FloatField()
    allocation1_a9 = models.FloatField()
    allocation1_b9 = models.FloatField()
    prob_A_1 = models.FloatField(initial =.1)
    prob_A_2 = models.FloatField(initial =.2)
    prob_A_3 = models.FloatField(initial =.3)
    prob_A_4 = models.FloatField(initial =.4)
    prob_A_5 = models.FloatField(initial =.5)
    prob_A_6 = models.FloatField(initial =.6)
    prob_A_7 = models.FloatField(initial =.7)
    prob_A_8 = models.FloatField(initial =.8)
    prob_A_9 = models.FloatField(initial =.9)

    def set_Allocations(self):
        self.allocation1_a1 = self.game1_slider1
        self.allocation1_b1 = 1-self.allocation1_a1
        self.allocation1_a2 = self.game1_slider2
        self.allocation1_b2 = 1-self.allocation1_a2
        self.allocation1_a3 = self.game1_slider3
        self.allocation1_b3 = 1-self.allocation1_a3
        self.allocation1_a4 = self.game1_slider4
        self.allocation1_b4 = 1-self.allocation1_a4
        self.allocation1_a5 = self.game1_slider5
        self.allocation1_b5 = 1-self.allocation1_a5
        self.allocation1_a6 = self.game1_slider6
        self.allocation1_b6 = 1-self.allocation1_a6
        self.allocation1_a7 = self.game1_slider7
        self.allocation1_b7 = 1-self.allocation1_a7
        self.allocation1_a8 = self.game1_slider8
        self.allocation1_b8 = 1-self.allocation1_a8
        self.allocation1_a9 = self.game1_slider9
        self.allocation1_b9 = 1-self.allocation1_a9


