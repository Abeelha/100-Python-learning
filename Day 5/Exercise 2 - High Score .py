# Theodoro Bertol Dev (Abeelha) #
# || Day 5 of #100DaysOfCode || #

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score
        
print(f"The highest score in the class is: {max_score}")





