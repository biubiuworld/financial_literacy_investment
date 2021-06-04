from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Group

class AssessmentInstruction(Page):
    pass

class FirstSkillQuestionPage1(Page):
    form_model = 'player'
    form_fields = ['part1_skill_question1','confidence_level_question1']
    def before_next_page(self):
        if Constants.correct_answer[0] == self.player.part1_skill_question1:
            self.player.num_of_correct_answers_part1 += 1


class FirstSkillQuestionPage2(Page):
    form_model = 'player'
    form_fields = ['part1_skill_question2','confidence_level_question2']
    def before_next_page(self):
        if Constants.correct_answer[1] == self.player.part1_skill_question2:
            self.player.num_of_correct_answers_part1 += 1


class FirstSkillQuestionPage3(Page):
    form_model = 'player'
    form_fields = ['part1_skill_question3','confidence_level_question3']
    def before_next_page(self):
        if Constants.correct_answer[2] == self.player.part1_skill_question3:
            self.player.num_of_correct_answers_part1 += 1


class FirstSkillQuestionPage4(Page):
    form_model = 'player'
    form_fields = ['part1_skill_question4','confidence_level_question4']
    def before_next_page(self):
        if Constants.correct_answer[3] == self.player.part1_skill_question4:
            self.player.num_of_correct_answers_part1 += 1


class FirstSkillQuestionPage5(Page):
    form_model = 'player'
    form_fields = ['part1_skill_question5','confidence_level_question5']
    def before_next_page(self):
        if Constants.correct_answer[4] == self.player.part1_skill_question5:
            self.player.num_of_correct_answers_part1 += 1
        self.participant.vars['num_of_correct_answers_part1'] = self.player.num_of_correct_answers_part1


class SkillTasksWaitPage(WaitPage):
    wait_for_all_groups = True


class SelfEvaluation(Page):
    form_model = 'player'
    form_fields = ['self_evaluation1', 'self_evaluation2']
    def before_next_page(self):
        self.participant.vars['self_evaluation1'] = self.player.self_evaluation1
        self.participant.vars['self_evaluation2'] = self.player.self_evaluation2

class SelfEvaluationWaitPage(WaitPage):
    after_all_players_arrive = "get_ranking"


page_sequence = [AssessmentInstruction, FirstSkillQuestionPage1, FirstSkillQuestionPage2, FirstSkillQuestionPage3,
                 FirstSkillQuestionPage4, FirstSkillQuestionPage5, SkillTasksWaitPage,
                 SelfEvaluation, SelfEvaluationWaitPage]
