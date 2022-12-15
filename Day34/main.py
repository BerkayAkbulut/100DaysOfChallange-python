import requests

from question_model import Question
#from data import question_data
from quiz_brain import QuizBrain

question_data=requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
question_data=question_data.json()
print(question_data)

question_bank = []
for question in question_data["results"]:
    #print(question)
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")