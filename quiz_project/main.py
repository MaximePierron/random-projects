from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html

question_bank = []

for question in question_data["results"]:
    question_bank.append(Question(html.unescape(question["question"]), question["correct_answer"]))


quiz = QuizBrain(question_bank)

quiz.play()
