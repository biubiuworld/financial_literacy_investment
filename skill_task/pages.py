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
            self.player.payoff = Constants.payment_per_correct_answer

class SkillTasksWaitPage(WaitPage):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False

    def after_all_players_arrive(self):
        pass

class SelfEvaluation(Page):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False

class SelfEvaluationWaitPage(WaitPage):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False

    def after_all_players_arrive(self):
        pass

class Control(Page):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False
    def is_treatment(self):
        return self.player.treatment_group == 0

class Treatment1(Page):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False
    def is_treatment(self):
        return self.player.treatment_group == 1

class Treatment2(Page):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False
    def is_treatment(self):
        return self.player.treatment_group == 2

class InvestmentInstruction(Page):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False

class InvestmentGame(Page):
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
    # def is_displayed(self):
    #     return False

    def vars_for_template(self):
        all_rounds = self.player.in_all_rounds()
        num_of_correct_answers = 0
        for player in all_rounds:
            num_of_correct_answers += player.payoff
        return {
                "num_of_correct_answers": num_of_correct_answers
        }


page_sequence = [
    Introduction, Presurvey, PreSurveyWaitPage, PreSurveyResult,
    AssessmentInstruction, SkillQuestionPage, SkillTasksWaitPage,
    SelfEvaluation, SelfEvaluationWaitPage,
    Control, Treatment1, Treatment2,
    InvestmentInstruction, InvestmentGame,
    Combinedresults]
