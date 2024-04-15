from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import os

os.system("cls|clear")

question_bank = []

for item in question_data:
    # question = Question(item['text'],item['answer'])
    question = Question(item['question'],item['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")