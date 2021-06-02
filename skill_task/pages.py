from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            return False

class Presurvey(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']

    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            return False

class PreSurveyWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'agg_gender'

    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            return False

class PreSurveyResult(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            return False
    def vars_for_template(self):
        return {
            'male_count': self.player.male_count,
            'female_count': self.player.female_count,
            'other_count': self.player.other_count,
            'dna_count': self.player.dna_count
        }

class AssessmentInstruction(Page):
    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            return False


    def before_next_page(self):
        self.participant.vars['score'] = 0

class SkillQuestionPage(Page):
    form_model = 'player'
    form_fields = ['answer','confidence']

    def answer_choices(self):
        return Constants.skill_question_choices[self.round_number - 1]


    def is_displayed(self):
        return True

    def vars_for_template(self):
        return {
            'questiontext': Constants.skill_question_text[self.round_number - 1]
        }



# check correct answers
    def before_next_page(self):
        #if self.player.answer == Constants.correct_answers[self.round_number - 1]:
        if Constants.correct_answers[self.round_number - 1] == self.player.answer:
            self.player.if_skill_question_correct = Constants.count_per_correct_answer
            self.participant.vars['score'] += 1
            self.player.num_of_correct_answers = self.participant.vars['score']
        else:
            self.player.num_of_correct_answers = self.participant.vars['score']


class SkillTasksWaitPage(WaitPage):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False

    wait_for_all_groups = True
    # after_all_players_arrive = 'agg_correct_answers'





class SelfEvaluation(Page):
    form_model = 'player'
    form_fields = ['self_evaluation1']
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False


class SelfEvaluationWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'grouping'
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False


class Control(Page):
    def is_displayed(self):
        if self.player.treatment_group == 0 and self.round_number == Constants.num_rounds:
            return True
        else:
            return False


class Treatment1(Page):
    def is_displayed(self):
        if self.player.treatment_group == 1 and self.round_number == Constants.num_rounds:
            return True
        else:
            return False
    def vars_for_template(self):
        return {
            'num_of_correct_answers': self.player.num_of_correct_answers
        }
  

class Treatment2(Page):
    def is_displayed(self):
        if self.player.treatment_group == 2 and self.round_number == Constants.num_rounds:
            return True
        else:
            return False
    def vars_for_template(self):
        return {
            'num_of_correct_answers': self.player.num_of_correct_answers
        }

class InvestmentInstruction(Page):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False

class InvestmentGame1(Page):
    form_model = 'player'
    form_fields = ['game_slider1']
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False
    def vars_for_template(self):
        return {
        'account_A': self.player.allocation_a1,
        'prob_A': self.player.prob_A_1,
        'prob_B': 1-self.player.prob_A_1,
        }

class InvestmentGame2(Page):
    form_model = 'player'
    form_fields = ['game_slider2']
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False
    def vars_for_template(self):
        return {
        'account_A': self.player.allocation_a2,
        'prob_A': self.player.prob_A_2,
        'prob_B': 1-self.player.prob_A_2,
        }

class InvestmentGame3(Page):
    form_model = 'player'
    form_fields = ['game_slider3']
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False
    def vars_for_template(self):
        return {
        'account_A': self.player.allocation_a3,
        'prob_A': self.player.prob_A_3,
        'prob_B': 1-self.player.prob_A_3,
        }

class InvestmentGame4(Page):
    form_model = 'player'
    form_fields = ['game_slider4']
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False
    def vars_for_template(self):
        return {
        'account_A': self.player.allocation_a4,
        'prob_A': self.player.prob_A_4,
        'prob_B': 1-self.player.prob_A_4,
        }

class InvestmentGame5(Page):
    form_model = 'player'
    form_fields = ['game_slider5']
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False
    def vars_for_template(self):
        return {
        'account_A': self.player.allocation_a5,
        'prob_A': self.player.prob_A_5,
        'prob_B': 1-self.player.prob_A_5,
        }

class InvestmentGame6(Page):
    form_model = 'player'
    form_fields = ['game_slider6']
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False
    def vars_for_template(self):
        return {
        'account_A': self.player.allocation_a6,
        'prob_A': self.player.prob_A_6,
        'prob_B': 1-self.player.prob_A_6,
        }

class InvestmentGame7(Page):
    form_model = 'player'
    form_fields = ['game_slider7']
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False
    def vars_for_template(self):
        return {
        'account_A': self.player.allocation_a7,
        'prob_A': self.player.prob_A_7,
        'prob_B': 1-self.player.prob_A_7,
        }

class InvestmentGame8(Page):
    form_model = 'player'
    form_fields = ['game_slider8']
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False
    def vars_for_template(self):
        return {
        'account_A': self.player.allocation_a8,
        'prob_A': self.player.prob_A_8,
        'prob_B': 1-self.player.prob_A_8,
        }

class InvestmentGame9(Page):
    form_model = 'player'
    form_fields = ['game_slider9']
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False
    def vars_for_template(self):
        return {
        'account_A': self.player.allocation_a9,
        'prob_A': self.player.prob_A_9,
        'prob_B': 1-self.player.prob_A_9,
        }
class InvestmentGameWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'set_Allocations'

    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False

class Combinedresults(Page):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False

    def vars_for_template(self):
        return {"num_of_correct_answers": self.player.num_of_correct_answers}

page_sequence = [
    Introduction, Presurvey, PreSurveyWaitPage, PreSurveyResult,
    AssessmentInstruction, SkillQuestionPage, SkillTasksWaitPage,
    SelfEvaluation, SelfEvaluationWaitPage, Combinedresults,
    Control, Treatment1, Treatment2,
    InvestmentInstruction, InvestmentGame1, InvestmentGame2, InvestmentGame3, InvestmentGame4, InvestmentGame5,
    InvestmentGame6, InvestmentGame7, InvestmentGame8, InvestmentGame9, InvestmentGameWaitPage,
    Combinedresults]
