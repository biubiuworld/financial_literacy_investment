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
    endowment_game1 = 3
    value_of_B_0p1_game1 = random.choices([3,0], weights = [1, 9])[0]
    value_of_B_0p2_game1 = random.choices([3,0], weights = [2, 8])[0]
    value_of_B_0p3_game1 = random.choices([3,0], weights = [3, 7])[0]
    value_of_B_0p4_game1 = random.choices([3,0], weights = [4, 6])[0]
    value_of_B_0p5_game1 = random.choices([3,0], weights = [5, 5])[0]
    value_of_B_0p6_game1 = random.choices([3,0], weights = [6, 4])[0]
    value_of_B_0p7_game1 = random.choices([3,0], weights = [7, 3])[0]
    value_of_B_0p8_game1 = random.choices([3,0], weights = [8, 2])[0]
    value_of_B_0p9_game1 = random.choices([3,0], weights = [9, 1])[0]

    top_value_of_B_0p1_game2 = random.choices([3,1], weights = [1, 9])[0]
    top_value_of_B_0p2_game2 = random.choices([3,1], weights = [2, 8])[0]
    top_value_of_B_0p3_game2 = random.choices([3,1], weights = [3, 7])[0]
    top_value_of_B_0p4_game2 = random.choices([3,1], weights = [4, 6])[0]
    top_value_of_B_0p5_game2 = random.choices([3,1], weights = [5, 5])[0]
    top_value_of_B_0p6_game2 = random.choices([3,1], weights = [6, 4])[0]
    top_value_of_B_0p7_game2 = random.choices([3,1], weights = [7, 3])[0]
    top_value_of_B_0p8_game2 = random.choices([3,1], weights = [8, 2])[0]
    top_value_of_B_0p9_game2 = random.choices([3,1], weights = [9, 1])[0]

    bottom_value_of_B_0p1_game2 = random.choices([1,0], weights = [1, 9])[0]
    bottom_value_of_B_0p2_game2 = random.choices([1,0], weights = [2, 8])[0]
    bottom_value_of_B_0p3_game2 = random.choices([1,0], weights = [3, 7])[0]
    bottom_value_of_B_0p4_game2 = random.choices([1,0], weights = [4, 6])[0]
    bottom_value_of_B_0p5_game2 = random.choices([1,0], weights = [5, 5])[0]
    bottom_value_of_B_0p6_game2 = random.choices([1,0], weights = [6, 4])[0]
    bottom_value_of_B_0p7_game2 = random.choices([1,0], weights = [7, 3])[0]
    bottom_value_of_B_0p8_game2 = random.choices([1,0], weights = [8, 2])[0]
    bottom_value_of_B_0p9_game2 = random.choices([1,0], weights = [9, 1])[0]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def get_payoff(self):
        # second investment game payoff
        for p in self.get_players():
            p.participant.vars['endowment_game1'] = p.participant.vars["num_of_correct_answers_part1"]
            p.participant.vars['value_of_B_0p1_game1'] = Constants.value_of_B_0p1_game1
            p.participant.vars['value_of_B_0p2_game1'] = Constants.value_of_B_0p2_game1
            p.participant.vars['value_of_B_0p3_game1'] = Constants.value_of_B_0p3_game1
            p.participant.vars['value_of_B_0p4_game1'] = Constants.value_of_B_0p4_game1
            p.participant.vars['value_of_B_0p5_game1'] = Constants.value_of_B_0p5_game1
            p.participant.vars['value_of_B_0p6_game1'] = Constants.value_of_B_0p6_game1
            p.participant.vars['value_of_B_0p7_game1'] = Constants.value_of_B_0p7_game1
            p.participant.vars['value_of_B_0p8_game1'] = Constants.value_of_B_0p8_game1
            p.participant.vars['value_of_B_0p9_game1'] = Constants.value_of_B_0p9_game1
        for p in self.get_players():
            p.participant.vars['payoff_game1_p10'] = round(p.participant.vars['endowment_game1']*(p.participant.vars['game1_slider1']*0.01*1 + (100-p.participant.vars['game1_slider1'])*0.01*p.participant.vars['value_of_B_0p1_game1']), 2)
            p.participant.vars['payoff_game1_p20'] = round(p.participant.vars['endowment_game1']*(p.participant.vars['game1_slider2']*0.01*1 + (100-p.participant.vars['game1_slider2'])*0.01*p.participant.vars['value_of_B_0p2_game1']), 2)
            p.participant.vars['payoff_game1_p30'] = round(p.participant.vars['endowment_game1']*(p.participant.vars['game1_slider3']*0.01*1 + (100-p.participant.vars['game1_slider3'])*0.01*p.participant.vars['value_of_B_0p3_game1']), 2)
            p.participant.vars['payoff_game1_p40'] = round(p.participant.vars['endowment_game1']*(p.participant.vars['game1_slider4']*0.01*1 + (100-p.participant.vars['game1_slider4'])*0.01*p.participant.vars['value_of_B_0p4_game1']), 2)
            p.participant.vars['payoff_game1_p50'] = round(p.participant.vars['endowment_game1']*(p.participant.vars['game1_slider5']*0.01*1 + (100-p.participant.vars['game1_slider5'])*0.01*p.participant.vars['value_of_B_0p5_game1']), 2)
            p.participant.vars['payoff_game1_p60'] = round(p.participant.vars['endowment_game1']*(p.participant.vars['game1_slider6']*0.01*1 + (100-p.participant.vars['game1_slider6'])*0.01*p.participant.vars['value_of_B_0p6_game1']), 2)
            p.participant.vars['payoff_game1_p70'] = round(p.participant.vars['endowment_game1']*(p.participant.vars['game1_slider7']*0.01*1 + (100-p.participant.vars['game1_slider7'])*0.01*p.participant.vars['value_of_B_0p7_game1']), 2)
            p.participant.vars['payoff_game1_p80'] = round(p.participant.vars['endowment_game1']*(p.participant.vars['game1_slider8']*0.01*1 + (100-p.participant.vars['game1_slider8'])*0.01*p.participant.vars['value_of_B_0p8_game1']), 2)
            p.participant.vars['payoff_game1_p90'] = round(p.participant.vars['endowment_game1']*(p.participant.vars['game1_slider9']*0.01*1 + (100-p.participant.vars['game1_slider9'])*0.01*p.participant.vars['value_of_B_0p9_game1']), 2)

        # second investment game payoff
        for p in self.get_players():
            p.participant.vars['endowment_game2'] = p.participant.vars["num_of_correct_answers_part2"]
        for p in self.get_players():
            if p.participant.vars['ranking_subgroup']>=50:
                p.participant.vars['value_of_B_0p1_game2'] = Constants.top_value_of_B_0p1_game2
                p.participant.vars['value_of_B_0p2_game2'] = Constants.top_value_of_B_0p2_game2
                p.participant.vars['value_of_B_0p3_game2'] = Constants.top_value_of_B_0p3_game2
                p.participant.vars['value_of_B_0p4_game2'] = Constants.top_value_of_B_0p4_game2
                p.participant.vars['value_of_B_0p5_game2'] = Constants.top_value_of_B_0p5_game2
                p.participant.vars['value_of_B_0p6_game2'] = Constants.top_value_of_B_0p6_game2
                p.participant.vars['value_of_B_0p7_game2'] = Constants.top_value_of_B_0p7_game2
                p.participant.vars['value_of_B_0p8_game2'] = Constants.top_value_of_B_0p8_game2
                p.participant.vars['value_of_B_0p9_game2'] = Constants.top_value_of_B_0p9_game2
            else:
                p.participant.vars['value_of_B_0p1_game2'] = Constants.bottom_value_of_B_0p1_game2
                p.participant.vars['value_of_B_0p2_game2'] = Constants.bottom_value_of_B_0p2_game2
                p.participant.vars['value_of_B_0p3_game2'] = Constants.bottom_value_of_B_0p3_game2
                p.participant.vars['value_of_B_0p4_game2'] = Constants.bottom_value_of_B_0p4_game2
                p.participant.vars['value_of_B_0p5_game2'] = Constants.bottom_value_of_B_0p5_game2
                p.participant.vars['value_of_B_0p6_game2'] = Constants.bottom_value_of_B_0p6_game2
                p.participant.vars['value_of_B_0p7_game2'] = Constants.bottom_value_of_B_0p7_game2
                p.participant.vars['value_of_B_0p8_game2'] = Constants.bottom_value_of_B_0p8_game2
                p.participant.vars['value_of_B_0p9_game2'] = Constants.bottom_value_of_B_0p9_game2

        for p in self.get_players():
            p.participant.vars['payoff_game2_p10'] = round(p.participant.vars['endowment_game2'] * (
                        p.participant.vars['game2_slider1'] * 0.01 * 1 + (
                            100 - p.participant.vars['game2_slider1']) * 0.01 * p.participant.vars[
                            'value_of_B_0p1_game2']), 2)
            p.participant.vars['payoff_game2_p20'] = round(p.participant.vars['endowment_game2'] * (
                        p.participant.vars['game2_slider2'] * 0.01 * 1 + (
                            100 - p.participant.vars['game2_slider2']) * 0.01 * p.participant.vars[
                            'value_of_B_0p2_game2']), 2)
            p.participant.vars['payoff_game2_p30'] = round(p.participant.vars['endowment_game2'] * (
                        p.participant.vars['game2_slider3'] * 0.01 * 1 + (
                            100 - p.participant.vars['game2_slider3']) * 0.01 * p.participant.vars[
                            'value_of_B_0p3_game2']), 2)
            p.participant.vars['payoff_game2_p40'] = round(p.participant.vars['endowment_game2'] * (
                        p.participant.vars['game2_slider4'] * 0.01 * 1 + (
                            100 - p.participant.vars['game2_slider4']) * 0.01 * p.participant.vars[
                            'value_of_B_0p4_game2']), 2)
            p.participant.vars['payoff_game2_p50'] = round(p.participant.vars['endowment_game2'] * (
                        p.participant.vars['game2_slider5'] * 0.01 * 1 + (
                            100 - p.participant.vars['game2_slider5']) * 0.01 * p.participant.vars[
                            'value_of_B_0p5_game2']), 2)
            p.participant.vars['payoff_game2_p60'] = round(p.participant.vars['endowment_game2'] * (
                        p.participant.vars['game2_slider6'] * 0.01 * 1 + (
                            100 - p.participant.vars['game2_slider6']) * 0.01 * p.participant.vars[
                            'value_of_B_0p6_game2']), 2)
            p.participant.vars['payoff_game2_p70'] = round(p.participant.vars['endowment_game2'] * (
                        p.participant.vars['game2_slider7'] * 0.01 * 1 + (
                            100 - p.participant.vars['game2_slider7']) * 0.01 * p.participant.vars[
                            'value_of_B_0p7_game2']), 2)
            p.participant.vars['payoff_game2_p80'] = round(p.participant.vars['endowment_game2'] * (
                        p.participant.vars['game2_slider8'] * 0.01 * 1 + (
                            100 - p.participant.vars['game2_slider8']) * 0.01 * p.participant.vars[
                            'value_of_B_0p8_game2']), 2)
            p.participant.vars['payoff_game2_p90'] = round(p.participant.vars['endowment_game2'] * (
                        p.participant.vars['game2_slider9'] * 0.01 * 1 + (
                            100 - p.participant.vars['game2_slider9']) * 0.01 * p.participant.vars[
                            'value_of_B_0p9_game2']), 2)


class Player(BasePlayer):
    pass


