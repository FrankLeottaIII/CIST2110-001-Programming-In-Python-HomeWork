# HW3.py
# Author: Frank R. Leotta III

# This Homework assignment is meant to test your ability to make functions within python as well as importing and using modules. This assignment might require you to do some research on your own. If you get stuck, try googling the problem, especially when it comes to importing and using the different modules.

# Question 1:
# Write a function that takes in a number and returns that number squared
# IE. If the user inputs 3, the function should return 9"""

""" THINGS TO DO
In problem 2 , see if you can def a funtion value that has no arguments
Solved
def my_function() -> int:
    # function code here
    return 42

next:


"""


def squared(varible)->int:
    """summery
    Discription: Squares a number

    Args:   varible (int): the number to be squared

    Returns:  int: the number squared
    """
    return int(varible) * int(varible)
squared(2)
# its going to be 4

# Question 2:
# Write a function that takes in a string, a letter, and a number and returns the string with the letter replaced at the number index
###MISSING TEXT



STRING_A = ""
LETTER_A = ""
NUMBER_A = 0
NUMBER_A = int(NUMBER_A)

def grab_string_letter_number(string: str,letter: str, number: int)->str:
    """summery
    Discription: grabs a string, letter, and number from the user and places them into 3 global varibles for later use.  USES GLOBAL VARIBLES
                This is to be used in the the replace_in_string funtion.

    global varibles: STRING_A, LETTER_A, NUMBER_A         

    Args:  string (str): the string to be changed
            letter (str): the letter to be replaced
            number (int): the index placepoint to replace the letter at in the string a for replace_in_string funtion 
                        example: 0 = first character, 1 = second character, etc in the index of the string
    Returns:  returns the string inputed by the user in a varible for later use

    Note: I used no global varibles, just assighn it to a varible outside this funtion

    """
    string = str(input("Enter a string: "))
    letter = str(input("Enter a letter: "))
    number = float(input("Enter a positive number: "))
    number = round(number)
    number = int(number)
    global STRING_A
    global LETTER_A
    global NUMBER_A
    STRING_A = string
    LETTER_A = letter
    NUMBER_A = number
    return STRING_A, LETTER_A, NUMBER_A


# grab_string_letter_number(STRING_A, LETTER_A, NUMBER_A)
# print(STRING_A, LETTER_A, NUMBER_A)


def str_to_list(varible: str)->list:
    """summery
    Discription: converts a string into a list

    Args:  varible (str): the string to be changed

    Returns:  list: the string converted into a list

    Note: I used no global varibles, just assighn it to a varible outside this funtion

    """
    list(varible)
    return  list(varible)

#test worked
STRING_A = " HELLO WORLD... AGAIN"
STRING_A = str_to_list(STRING_A)#  need to assighn it to a varible
print(STRING_A)

def count_characters(varible: list)->int:
    """summery
    Discription: counts the number of characters in a list, used forin replace_in_string funtion

    Args:  varible (str): the string to be changed

    Returns:  int: the number of characters in a string

    Note: I used no global varibles, just assighn it to a varible outside this funtion

    """
    len(varible)
    return  len(varible)

Characters = 0
Characters = count_characters(STRING_A)
print(Characters)

def replace_in_string()->str:
    global STRING_A
    global LETTER_A
    global NUMBER_A
    grab_string_letter_number(STRING_A, LETTER_A, NUMBER_A)
    STRING_A = str_to_list(STRING_A)
    varible = 0
    varible = count_characters(STRING_A)
    if NUMBER_A <= varible == True:
        NUMBER_A-=1
    if IndexError:     
        NUMBER_A-=1
        STRING_A[NUMBER_A] = LETTER_A
        STRING_A = "".join(STRING_A)
        return print(STRING_A), STRING_A

replace_in_string()

#Sidenote: I need a more streamlined way of keeping notes... 
# perhaps a file specifically for quicknotes for funtions in my code seperate to glance at




user_number = 0

a = None
b = None
c = None

# Question 3:
# Write a function that takes in a number, a lower bound, and an upper bound and returns whether the number is within the bounds
# IE. If the user inputs 5, 1, and 10, the function should return True
#global varibles for this funtion
USER_NUMBER = 0
LOW_BOUND = 0
HIGH_BOUND = 0


def is_in_bounds_data()->int:
    """summery
    Discription: grabs 3 imput answers from user and puts it into global varibles.  It will be used in the is_in_bounds funtion

    global varibles: USER_NUMBER, LOW_BOUND, HIGH_BOUND

    Args:none

    Returns:  bool: returns true if the number is between the two other numbers, false if not
    
    """
    global USER_NUMBER
    global LOW_BOUND
    global HIGH_BOUND
    USER_NUMBER = input("Enter a number: ")
    LOW_BOUND = input("Enter a low number: ")
    HIGH_BOUND = input("Enter a high number: ")
    return USER_NUMBER, LOW_BOUND, HIGH_BOUND

def is_in_bounds()->bool:

    """summery
    Discription: checks if a number is between two other numbers
    Uses the global varibles from is_in_bounds_data funtion
    low bound is the lowest number, high bound is the highest number, user number is the number to be checked

    global varibles: USER_NUMBER, LOW_BOUND, HIGH_BOUND

    Args:none

    """
    global USER_NUMBER
    global LOW_BOUND
    global HIGH_BOUND
    varible = USER_NUMBER
    low_bound = LOW_BOUND
    high_bound = HIGH_BOUND
    if varible >= low_bound and varible <= high_bound:
        return True
    elif varible < low_bound or varible > high_bound:
        return False

# Question 4:
# Write a function that asks the user for their name, age, and favorite color. Then write a function that accepts those three parameters and prints them out in a sentence
# IE. If the user inputs "John", 20, and "blue", the function should print "Hello, my name is John. I am 20 years old. My favorite color is blue."
# Hints: You will need to use the input() function to get the user's input. You will also need to use the str() function to convert the age to a string
# This is a two part question. You will need to write two functions
# remember in class we learned you can return miltiple values from a function
# also remember in class you can pass in pultiple variables into a function

NAME = ""
AGE = 0
AGE= int(AGE)
COLOR = ""
def get_name_age_color()->str:
    global NAME
    global AGE
    global COLOR
    NAME = input("Enter your name: ")
    AGE = input("Enter your age: ")
    COLOR = input("Enter your favorite color: ")
    return str(NAME), str(AGE), str(COLOR)
get_name_age_color()
def print_name_age_color()->str:
    global NAME
    global AGE
    global COLOR
    return print("hello there, my name is " + NAME + ".  I am " + str(AGE) + " years old, and my favorate color is " + COLOR + ".")
print_name_age_color()

# Question 5:
# import the random module and use it to generate a random number between 1 and 100
import random
print(random.randint(1,100))
#printed the random number generated.  The number is not saved since the question did not speficly ask for it to be saved

# Question 6:
# import the math module and use it to find the square root of 16 (hint: use the sqrt() function)
import math
sushi= 1
sushi=float(sushi)
sushi= math.sqrt(16)
print(float(sushi))


# Question 7:
# import the sys module and use it to display the version of python you are using
# this time import the module using the import "as" keyword
# hint: use the version attribute (sys.version)
import sys as system
print(system.version)

# Question 8:
# import the os module and use it to display the current working directory. This time import the module using the from keyword
# hint: use the getcwd() function
from os import getcwd
print(getcwd())


"""