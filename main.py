from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for i in question_data:
    text = Question(i["text"], i["answer"])
    question_bank.append(text)

questions = Quizbrain(question_bank)
questions.new_question()

print("You have completed the quiz!")
print(f"Your final score is {questions.score}/{questions.question_number}")