print("Welcome to the Quiz Game")

playing = input("Do you want to play (yes/no)? ")

if playing.lower() != "yes":
    quit()

score = 0

print("Okay! let's play")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("InCorrect!")


answer = input("What does GPU stand for? ").lower()
if answer == "graphic processing unit":
    print("Correct!")
    score+=1

else:
    print("InCorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score+=1

else:
    print("InCorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print("Correct!")
    score+=1

else:
    print("InCorrect!")


print("Your score is: "+ str(score))