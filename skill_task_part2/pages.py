from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class AssessmentInstruction(Page):
    pass

class SecondSkillQuestionPage1(Page):
    form_model = 'player'
    form_fields = ['part2_skill_question1','part2_confidence_level_question1']
    def before_next_page(self):
        if Constants.correct_answer[0] == self.player.part2_skill_question1:
            self.player.num_of_correct_answers_part2 += 1

class SecondSkillQuestionPage2(Page):
    form_model = 'player'
    form_fields = ['part2_skill_question2','part2_confidence_level_question2']
    def before_next_page(self):
        if Constants.correct_answer[1] == self.player.part2_skill_question2:
            self.player.num_of_correct_answers_part2 += 1

class SecondSkillQuestionPage3(Page):
    form_model = 'player'
    form_fields = ['part2_skill_question3','part2_confidence_level_question3']
    def before_next_page(self):
        if Constants.correct_answer[2] == self.player.part2_skill_question3:
            self.player.num_of_correct_answers_part2 += 1

class SecondSkillQuestionPage4(Page):
    form_model = 'player'
    form_fields = ['part2_skill_question4','part2_confidence_level_question4']
    def before_next_page(self):
        if Constants.correct_answer[3] == self.player.part2_skill_question4:
            self.player.num_of_correct_answers_part2 += 1

class SecondSkillQuestionPage5(Page):
    form_model = 'player'
    form_fields = ['part2_skill_question5','part2_confidence_level_question5']
    def before_next_page(self):
        if Constants.correct_answer[4] == self.player.part2_skill_question5:
            self.player.num_of_correct_answers_part2 += 1
        self.participant.vars['num_of_correct_answers_part2'] = self.player.num_of_correct_answers_part2


class SkillTasksWaitPage(WaitPage):
    wait_for_all_groups = True


class Results(Page):
    pass


page_sequence = [AssessmentInstruction, SecondSkillQuestionPage1, SecondSkillQuestionPage2, SecondSkillQuestionPage3,
                 SecondSkillQuestionPage4, SecondSkillQuestionPage5, SkillTasksWaitPage, Results]
