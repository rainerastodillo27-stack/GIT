#python quiz game

questions = ("How old are you?: ",
             "Which year you were born?: ",
             "What is your name?: ",
             "Where do you live?: ",
             "What is you favorite food?: ")

options = (("A. 18", "B. 20", "C. 21", "D. 33"),
           ("A. 2004", "B. 2010", "C. 2011", "D. 2019"),
           ("A. ALEX", "B. RAINER", "C. TRISTAN", "D. SOBEE"),
           ("A. TALIS", "B. SILAY", "C. BACOLOD", "D. VICTORIAS"),
           ("A. hotdog", "B. burger", "C. fries", "D. donut"))

answers = ("C", "A", "B", "C", "C")
guesses = []
score = 0
question_num = 0


for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("Correct")

    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the Correct answers")

    question_num += 1



print("----------------------")

print("        RESULT        ")

print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()    


print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()    

score = int(score / len(question) * 100)
print(f"Your score is : {score}%")








#---Other way (dict)--
#quiz = [
# {
#  "question" : "What's my age?",
#  "choices" : [10, 23, 45, 9000]
# },
#...
#]