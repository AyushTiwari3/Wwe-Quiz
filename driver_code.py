from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]

name  = input("enter your name:")
print(f"welcome {name} to the quiz game")
scores = open(f"{name}.txt","a")

print("This is a quiz designed written in python and this quiz is about the World Famous WWE")








for question in question_data:
  question_text=question["question"]
  question_answer=question["correct_answer"]
  n_question=Question(question_text,question_answer)
  question_bank.append(n_question)
quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
  quiz.next_question()
print("You've completed the quiz")
print(f"Your final score for this attempt is {quiz.score}/{quiz.question_number}")
scores.write(f"Quiz Score : {quiz.score}\n")


flag = input("press '1' to view the records of all quiz attempts else press '2' TO EXIT ")


if flag == "1" :
  scores.close()
  scores = open(f"{name}.txt","r")
  print(scores.read())

print("Thank you For attempting this quiz")




scores.close()




