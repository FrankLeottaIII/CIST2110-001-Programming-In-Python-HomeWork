#Project1.py
# Author: Frank R. Leotta III
"""
#notes, removed, Now need to check if all questions are good
##while loop is contained 
had an error i could not fix.  reverted to older code saved
OK i am saving it so I have a savepoint.... 

"""
# This project is meant to test your ability from everything we have learned so far in class
# You will need to use variables, if statements, loops, and functions

# Quiz Game:
# Create a simple console-based quiz game where the user answers a series of questions.
# The game should keep track of the user's score and provide feedback based on the answers given.

# Write a function that displays a welcome message to the user and explains the rules of the game
def welcome():
    print("Welcome to the quiz game")
    print("You will be asked a series of questions and given 4 options to choose from")
    print("You will be awarded 1 point for every correct answer and 0 points for every incorrect answer")
    print("Good luck!")
    print("")

# Implement at least 5 questions, each with 4 answer options (a, b, c, d). Each question should be worth 1 point.
# For each question, display the question and the answer options to the user.
# Use input() to get the user's answer.
# Use if or if-else statements to check if the answer is correct.
# If the answer is correct, display a positive feedback message and add points to the user's score.
# If the answer is incorrect, display a negative feedback message and provide the correct answer.
# Score Tracking:


# Keep track of the user's score throughout the game.
# After all questions have been answered, display the user's total score and a farewell message.
# Function Utilization:
SCORE = 0
def score_now(varible:bool, SCORE:int):
    SCORE
    if varible == True:
        SCORE = SCORE + 1
        print("yours score now is now" + str(SCORE))
        return SCORE
    if varible == False:
        SCORE = SCORE + 0
        print("yours score now is now" + str(SCORE))
        return SCORE
    else:
        print("error")
        print("yours score now is now: " + str(SCORE))  
        return SCORE


# Create a function to ask a question and check the answer. This function should accept parameters like the question, options, and the correct answer, and return whether the user was correct.
# an example would be def ask_question(question, option_1, option_2, option_3, option_4, correct_answer):
# the return value should be a boolean (True or False) for whether the user was correct
def ask_question(question:str, option_1:str, option_2: str, option_3: str, option_4: str, correct_answer: str) -> bool:
    print(question)
    print(str(option_1.lower()))
    option_1 = "a"
    print(str(option_2.lower()))
    option_2 = "b"
    print(str(option_3.lower()))
    option_3 = "c"
    print(str(option_4.lower()))
    option_4 = "d"
    answer = input("Your answer:")
    answer = answer.upper()
    while answer != "a" and answer != "b" and answer != "c" and answer != "d" and answer != "A" and answer != "B" and answer != "C" and answer != "D" and answer != ("skip") and answer != ("SKIP"):
        print("That is not a valid answer, please try again")
        answer = input("Your answer:")
        answer = answer.upper()
    if answer == correct_answer:
        print("Correct!")
        return True
    if answer == ("skip") or answer == ("SKIP"):
        print("You have chosen to skip this question")
        return False

    else:
        correct_answer = correct_answer.upper()
        print("Incorrect, the correct answer was " + correct_answer.upper())
        return False

    
print("testing below")

q1 = ask_question("1.) Which tree is part of the red oak subspecies?", "A. white oak", "B. black oak", "C. red maple", "D. chestnut oak", "B")
score_now(q1, SCORE)
q2 = ask_question("2.) Which tree is part of the white oak subspecies?", "A. post oak", "B. scarlet oak", "C. silver maple", "D. willow oak", "A")
q3 = ask_question("3.) In ecological silviculture, what is NOT true about the selection system?", "A. it is a silvicultural system that maintains uneven aged stands.", "B. Often represented by “reverse J” dia. distrib. or something slightly more irregular", "C. It is a silvicultural system that maintains even aged stands.", "D. It is a silvicultural system that includes 3 or more age classes of trees.", "C")
q4 = ask_question("4.) what is NOT true about the B-D-q method?", "A.  it provides a guiding curve approach", "B.  applies to group selection", "C.  applies to single tree selection", "D.  it uses a ratio of small tree to large trees in its calculations", "B")
q5 = ask_question("5.) What does the D stand for in the B-D-q method?", "A.  diameter", "B.  Largest density class in the residual stand", "C.  Largest diameter class in the residual stand", "D.  diameter ratio", "C")


# Create a function to display the final score, which takes the score as a parameter and displays a message.
def final_score():

    print("Your final score is " + str(SCORE) + " out of 5")
    if SCORE == 10:
        print("one hundred percent! Perfect score!")
    elif SCORE == 4:
        print("80 percent Great job!")
    elif SCORE == 3:
        print("you passed, but just by the skin of your teeth!")
    elif SCORE == 2:
        print("Not bad!")
    elif SCORE == 1:
        print("You can do better!")
    else:
        print("Better luck next time!")
    print("")
    print("Thank you for playing!")
# Loops:
# Use a for or while loop to iterate through the questions.
# Variable Casting:
# Ensure that user input is cast and checked appropriately to avoid errors during execution.
# Error Handling:
# Implement basic error handling to manage invalid inputs from the user (e.g., an answer other than a, b, c, or d).
