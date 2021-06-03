from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class AssessmentInstruction(Page):
    pass

class FirstSkillQuestionPage1(Page):
    form_model = 'player'
    form_fields = ['part1_skill_question1','confidence_level_question1']
    def before_next_page(self):
        if Constants.correct_answer[0] == self.player.part1_skill_question1:
            self.player.num_of_correct_answers_part1 += 1
            # self.participant.vars['num_of_correct_answers_part1'] += 1
            # self.player.num_of_correct_answers_part1 = self.participant.vars['num_of_correct_answers_part1']

class FirstSkillQuestionPage2(Page):
    form_model = 'player'
    form_fields = ['part1_skill_question2','confidence_level_question2']
    def before_next_page(self):
        if Constants.correct_answer[1] == self.player.part1_skill_question2:
            self.player.num_of_correct_answers_part1 += 1
            # self.participant.vars['num_of_correct_answers_part1'] += 1
            # self.player.num_of_correct_answers_part1 = self.participant.vars['num_of_correct_answers_part1']

class FirstSkillQuestionPage3(Page):
    form_model = 'player'
    form_fields = ['part1_skill_question3','confidence_level_question3']
    def before_next_page(self):
        if Constants.correct_answer[2] == self.player.part1_skill_question3:
            self.player.num_of_correct_answers_part1 += 1
            # self.participant.vars['num_of_correct_answers_part1'] += 1
            # self.player.num_of_correct_answers_part1 = self.participant.vars['num_of_correct_answers_part1']

class FirstSkillQuestionPage4(Page):
    form_model = 'player'
    form_fields = ['part1_skill_question4','confidence_level_question4']
    def before_next_page(self):
        if Constants.correct_answer[3] == self.player.part1_skill_question4:
            self.player.num_of_correct_answers_part1 += 1
            # self.participant.vars['num_of_correct_answers_part1'] += 1
            # self.player.num_of_correct_answers_part1 = self.participant.vars['num_of_correct_answers_part1']

class FirstSkillQuestionPage5(Page):
    form_model = 'player'
    form_fields = ['part1_skill_question5','confidence_level_question5']
    def before_next_page(self):
        if Constants.correct_answer[4] == self.player.part1_skill_question5:
            self.player.num_of_correct_answers_part1 += 1
        self.participant.vars['num_of_correct_answers_part1'] = self.player.num_of_correct_answers_part1
            # self.participant.vars['num_of_correct_answers_part1'] += 1
            # self.player.num_of_correct_answers_part1 = self.participant.vars['num_of_correct_answers_part1']

class SkillTasksWaitPage(WaitPage):
    wait_for_all_groups = True


class SelfEvaluation(Page):
    form_model = 'player'
    form_fields = ['self_evaluation1', 'self_evaluation2']

class SelfEvaluationWaitPage(WaitPage):
    wait_for_all_groups = True


class Control(Page):
    def is_displayed(self):
        if self.player.treatment_group == 0:
            return True
        else:
            return False


class Treatment1(Page):
    def is_displayed(self):
        if self.player.treatment_group == 1:
            return True
        else:
            return False

    def vars_for_template(self):
        return {
            'num_of_correct_answers': self.player.num_of_correct_answers_part1
        }


class Treatment2(Page):
    def is_displayed(self):
        if self.player.treatment_group == 2:
            return True
        else:
            return False

    def vars_for_template(self):
        return {
            'num_of_correct_answers': self.player.num_of_correct_answers_part1
        }




page_sequence = [AssessmentInstruction, FirstSkillQuestionPage1, FirstSkillQuestionPage2, FirstSkillQuestionPage3,
                 FirstSkillQuestionPage4, FirstSkillQuestionPage5, SkillTasksWaitPage,
                 SelfEvaluation, SelfEvaluationWaitPage,
                 Control, Treatment1, Treatment2]
