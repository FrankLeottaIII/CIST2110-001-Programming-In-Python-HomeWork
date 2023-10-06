# Project1.py
# Author: Frank R. Leotta III


# This project is meant to test your ability from everything we have learned so far in class
# You will need to use variables, if statements, loops, and functions

# Quiz Game:
# Create a simple console-based quiz game where the user answers a series of questions.
# The game should keep track of the user's score and provide feedback based on the answers given.

# Write a function that displays a welcome message to the user and explains the rules of the game
print("Hello, welcome to my quiz game.")
print(" I will be asking you a few questions, and keeping score, so try your best!")
print("please enter the letter of the answer you think is correct, or it will regester as incorrect.")
# Implement at least 5 questions, each with 4 answer options (a, b, c, d). Each question should be worth 1 point.
# For each question, display the question and the answer options to the user.
# Use input() to get the user's answer.
# Use if or if-else statements to check if the answer is correct.
# If the answer is correct, display a positive feedback message and add points to the user's score.
# If the answer is incorrect, display a negative feedback message and provide the correct answer.
# Score Tracking:
scores = 0

SCORE = 0
answer = ""
correct_answer = ""
def ask_question(question, option_1, option_2, option_3, option_4,answer,scores: int) -> str:
        """_summary_
        
        This function is designed to ask the user a question, and convert the answer to a simple letter string
            
            Args:
            question: The question being asked
            option_1: the first option for the user to choose from
            option_2: the second option for the user to choose from
            option_3: the third option for the user to choose from
            option_4: the fourth option for the user to choose from
            correct_answer: the correct answer to the question
            SCORE: the score of the user
  
            """
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
        if answer == correct_answer:   
                print("Correct!")
                return True
        else:   
                print("Incorrect, the correct answer was " + correct_answer)
                return False
## cant combine the two functions (counter and answer), it will not work, it will not return the correct answer, it will return the answer the user gave
## probably for the best, it would be a mess to try and combine them

def TFcounter(SCORE: int) -> int:
        """_summary_
        
        This function is designed to count the score of the user using boolean values
            
            Args:
            none
  
            """
        if True:   
                SCORE += 1
        elif False:   
                SCORE += 0
        Return: print( str(SCORE) + " is your score so far")
        
print(scores)
        

first = ask_question("Which of these trees is part of the red oak subspecies?", "white oak", "black oak", "red maple", "red oak", answer)
while first == True:
        scores += 1
        print(scores)
        break
else:
        scores += 0
        print(scores)
        break
find_answer_right("red oak", answer, score)
print(str(score) + " is your score so far")
print("The correct answer is" + correct_answer)

          





# Keep track of the user's score throughout the game.
# After all questions have been answered, display the user's total score and a farewell message.
# Function Utilization:

# Create a function to ask a question and check the answer. This function should accept parameters like the question, options, and the correct answer, and return whether the user was correct.
# an example would be def ask_question(question, option_1, option_2, option_3, option_4, correct_answer):
# the return value should be a boolean (True or False) for whether the user was correct

# Create a function to display the final score, which takes the score as a parameter and displays a message.
# Loops:
# Use a for or while loop to iterate through the questions.
# Variable Casting:
# Ensure that user input is cast and checked appropriately to avoid errors during execution.
# Error Handling:
# Implement basic error handling to manage invalid inputs from the user (e.g., an answer other than a, b, c, or d).

