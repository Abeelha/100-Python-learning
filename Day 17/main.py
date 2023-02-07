# Theodoro Bertol Dev (Abeelha) #
# || Day 17 of #100DaysOfCode || #

from multiprocessing.connection import answer_challenge
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    question_text = questions["text"]
    question_answer = questions["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
    
print(f"You've completed the quiz!\nYour final score was: {quiz.score}/{quiz.question_number}")