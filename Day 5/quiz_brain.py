class Quizbrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question= self.question_list[self.question_number].question
        answer = self.question_list[self.question_number].correct_answer
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number}:  {question} (True/False)?:").lower()
        self.check_answer(user_answer, answer)

    def still_has_question(self):
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False
        return self.question_number < len(self.question_list)
        

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it! Here is  your score {self.score}/{len(self.question_list)} times.")
        else:
            print(f"I'm sorry, you're wrong. Here is  your score {self.score}/{len(self.question_list)} times.")