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
CHARACTERS = 0
CHARACTERS = count_characters(STRING_A)
print(CHARACTERS)

def replace_in_string(STRING_A, LETTER_A, NUMBER_A)
        





####  CODE for main funtion###
# grab_string_letter_number(STRING_A, LETTER_A, NUMBER_A)
# print(STRING_A, LETTER_A, NUMBER_A)





"""
grab_string_letter_number(string, letter, number)

replace_in_string()
"""



"""
sentence = str(input("Enter a string: "))
letter = str(input("Enter a letter: "))
number = float(input("Enter a number. It will be rounded: "))
number = round(number)
number = int(number)
sentence= list(sentence)
"""


""" this is the part that got me for a bit:, need to remember this idiotproofing method
counting = len(sentence)
checking = number - 1
#this is the part that got me for  bit:
checking = len(sentence)
if checking <= number == True:
    number-=1
if IndexError:   
    number-=1
# holy crap that was aggravating, but it works now.  This is a good code to idiotproof it
sentence[number] = letter  #replaces the letter at the index with the varible number, which is what was inputed
sentence = "".join(sentence) #joins the list back into a string
print(sentence)
"""

"""code not working
while counting <= checking:
    print("The number you inputed is larger than the string you inputed, please try again")
    number = float(input("Enter a number. It will be rounded: "))
    number = round(number)
    number = int(number)
else:
    print("good")
    len(sentence)
    sentence[number] = letter  #replaces the letter at the index with the varible number, which is what was inputed
    sentence = "".join(sentence) #joins the list back into a string
"""
#got via copilot

# def replaced(string:str, letter:str, number:int)->str:
#     """summery
#     Discription: replaces a letter in a string, any floats will be rounded to the nearest whole number

#     Args:   string (str): the string to be changed
#         letter (str): the letter to be replaced
#         number (int): the index to replace the letter at

#     Returns:  str: the string with the letter replaced
#     """
#     string_list = list(string)
#     string_list[number] = letter
#     return ''.join(string_list)

# replaced(string, letter, number)
#got via copilot
#  def replace(string, letter, number)->str:
#     """summery
#     Discription: replaces a letter in a string at a given index

#     Args:   string (str): the string to be changed
#             letter (str): the letter to be replaced
#             number (int): the index to replace the letter at

#     Returns:  str: the string with the letter replaced
#     """
#     return string[:number] + letter + string[number+1:]


#ok you know what, ill just reverse engineer what copilot gave me

# def replace(string, letter, number)->str:
#     """summery
#     Discription: replaces a letter in a string at a given index



# Question 3:
# Write a function that takes in a number, a lower bound, and an upper bound and returns whether the number is within the bounds
# IE. If the user inputs 5, 1, and 10, the function should return True

# Question 4:
# Write a function that asks the user for their name, age, and favorite color. Then write a function that accepts those three parameters and prints them out in a sentence
# IE. If the user inputs "John", 20, and "blue", the function should print "Hello, my name is John. I am 20 years old. My favorite color is blue."
# Hints: You will need to use the input() function to get the user's input. You will also need to use the str() function to convert the age to a string
# This is a two part question. You will need to write two functions
# remember in class we learned you can return miltiple values from a function
# also remember in class you can pass in pultiple variables into a function
"""
NAME= “”
AGE = 0
COLOR=
name


T=true
While T = true
     If  break
     Edit break
Elsif break
 Else 

"""


# Question 5:
# import the random module and use it to generate a random number between 1 and 100
"""Pip install random
Import random
Random(1,100)
"""


# Question 6:
# import the math module and use it to find the square root of 16 (hint: use the sqrt() function)
"""Def square_root(varible)->float
Import math
Sushi=1.0
Sushi=float(sushi)
Sushi= math.sqrt(varible)
  Return print(float(sushi))

"""

# Question 7:
# import the sys module and use it to display the version of python you are using
# this time import the module using the import "as" keyword
# hint: use the version attribute (sys.version)
"""


"""
# Question 8:
# import the os module and use it to display the current working directory. This time import the module using the from keyword
# hint: use the getcwd() function
"""
Import os
From os get getcwd()
Print()


"""