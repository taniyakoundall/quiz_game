from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    ques_text = question["question"]
    ques_answer = question["correct_answer"]
    new_q = Question(ques_text, ques_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_ques():
    quiz.next_question()

print(f"You completed the quiz with final score {quiz.score}/{quiz.question_number}")