
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_ques(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q{self.question_number}: {current_q.text}? ('True'/'False')")
        self.check_answer(user_ans, current_q.answer)
    def check_answer(self, u, ca):
        if u.lower() == ca.lower():
            self.score += 1
            print("You got it right!!")
        else:
            print("You got it wrong..")
        print(f"the correct answer was {ca}.")
        print(f"Your total score is {self.score}/{self.question_number}.")
        print("\n")
