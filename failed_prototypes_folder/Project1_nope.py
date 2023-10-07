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

#while True:
 #       SCORE = 0
  ##      quiz = 0
    #    print("Question 1")
     #   ask_question("What is the most common tree in the United States?")
      #  a_letter("white oak", "black oak", "red maple", "red oak")
       # answer = input()
        #if answer == "d":
         #       print("Correct!")
          #      SCORE += 1
           #     break
#        else:
#                print("Incorrect, the correct answer is red oak")
 #               break
#starting varibles----------------------------------------------------------------------------------------------------------------
SCORE = 0
quiz = 0
A = ""
B = ""
C = ""
D = ""
answer = ""
CORRECT_ANSWER = ""
first =""
second =""
third =""
fourth =""
fifth =""
Sixth =""
Seventh =""
Eighth =""
Ninth =""
Tenth =""
#___________________________________________________________________________________________________________________________

##BROKEN FUNCTIONs###
#def find_answer_right(CORRECT_ANSWER: str, answer: str, SCORE: int) -> int:

### Defined Functions ###------------
"""def find_answer_right(CORRECT_ANSWER: str, answer: str, SCORE: int) -> int:
        _summary_
        
#        This function is designed to check if the user's answer is correct and give them a point if it is
            
#            Args:
            CORRECT_ANSWER: The correct answer
            answer: The user's answer
            SCORE: The user's score

  
            
        if answer == CORRECT_ANSWER:
                print("Correct!")
                SCORE += 1
                return SCORE
        else:
                print("Incorrect, the correct answer is " + CORRECT_ANSWER)
                return SCORE
                """
##example of how to use this function
##find_answer_right(imput(), answer,<which would be a b c or de beforehand>, SCORE)   
#answer = input("what is the second letter of the alphabet?")
#answer = answer.upper() 
#CORRECT_ANSWER = B
#find_answer_right( CORRECT_ANSWER, answer, SCORE)  


def ask_question(question: str) -> str:
        """_summary_
        
        This function is designed to ask the user a question, and convert the answer to a simple letter string
            
            Args:
            question: The question being asked

  
            """
        print(question)






def a_letter(A: str, B: str, C: str, D: str) -> str:

        """_summary_
        
        This function assighns a value to multible choice and  
        adds a letter and period to make the question's multible choice look better
            
            Args:
            type: The question being asked

  
            """
        print("a. " + A)
        print("b. " + B)
        print("c. " + C)
        print("d. " + D)

        return  ("a. " + A), ("b. " + B), ("c. " + C), ("d. " + D)
print(SCORE)
        
a_letter("white oak", "black oak", "red maple", "red oak")








#while first == True:
#        scores += 1
#        print(scores)
#        break
#else:
#        scores += 0
#        print(scores)
#        break
#find_answer_right("red oak", answer, SCORE)




          
#while quiz < 5:
#        quiz += 1




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

