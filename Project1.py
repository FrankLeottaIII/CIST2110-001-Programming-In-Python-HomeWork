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



score = 0
def ask_question(question, option_1, option_2, option_3, option_4, correct_answer):
        print(question)
        print(option_1.lower())
        option_1 = "a"
        print(option_2.lower())
        option_2 = "b"
        print(option_3.lower())
        option_3 = "c"
        print(option_4.lower())
        option_4 = "d"
        answer = input("Your answer:")
        if answer == correct_answer:
                print("Correct!")
                return score += 1 
        else:
                print("Incorrect, the correct answer was " + correct_answer)
                return score += 0 
        

print(ask_question("Which species of oak tree is part of the red oak subspecies?", "a. White Oak", "b. black Oak", "c. post Oak", "d. red Maple", "b. black Oak"))

answer = imput("Your answer:")
if answer_A == "c": 
        print("Correct!")
        score += 1  
else:   
        print("Incorrect, the correct answer was c. post Oak")
        score += 0
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
