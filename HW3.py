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


#attempt 1
# def square()->int:
#     global user_input1
#     user_input1 = input("Enter a number: ")
#     while user_input1 != int:
#         print("Please enter a number")
#         user_input1 = input("Enter a number: ")
#     if user_input1 == int:
#         return user_input1 ** 2 
#              break
#     else:   
#         return 0  
 ## above does not work, something to do with the while loop not working as intended or the ** malfuntioning when 
 # checked in jupiter...     

#attempt 2
# def squared()->int:
#     global user_input1
#     user_input1 = input("Enter a number: ")
#     while user_input1 != int == False:
#         print("Please enter a number")
#         user_input1 = input("Enter a number: ")
#     return user_input1 * user_input1, print(user_input1 * user_input1)
# ## above does not work, something to do with the while loop not working as intended 
 

##found via copilot... really wanted to figure it out myself
# user_input1 = 0
# def squared()->int:
#     global user_input1
#     user_input1 = input("Enter a number: ")
#     while not user_input1.isdigit():
#         print("You mistyped.  Please enter a number")
#         user_input1 = input("Enter a number: ")
#     return print(int(user_input1) * int(user_input1)), int(user_input1) * int(user_input1)


### no, something is wrong, the funtion should end up taking in a number and returning that number squared in the()
# def squared(varible)->int:
#     while not varible.isdigit():
#         print("You mistyped.  Please enter a number")
#         varible = input("Enter a number: ")
#     int(varible) * int(varible)
#     return  int(varible) * int(varible)
#b = 2
#squared(b)
#nope doesnt work... ill stop complecating it and just do it the easy way
##yea, i just wasted time dealing with this, attributeError: 'int' object has no attribute 'isdigit'... so it wouldn't work anyway to prevent accedental input of a letter or word when coding for a number...
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
# IE. If the user inputs "Hello World", "a", and 3, the function should return "Helao World"
#
#def replace(string:str, letter:str, number:int)->str: """ did not need these varibles,  this is for a differnt use"""

#attempt 1

def replace_in_string()->str:
    """summery
    Discription: replaces a letter in a string, any floats will be rounded to the nearest whole number

    Args:  string (str): the string to be changed

    Returns:  str: the string with the letter replaced
    """
    sentence = str(input("Enter a string: "))
    letter = str(input("Enter a letter: "))
    number = float(input("Enter a positive number: "))
    number = round(number)
    number = int(number)
    sentence= list(sentence)
    count_characters = len[sentence]
    count_characters = int(count_characters)
    if count_characters < number:
        print("The number you inputed is larger than the string you inputed, please try again")
        replace_in_string(sentence, letter, number)
    len(sentence)
    sentence[number] = letter  #replaces the letter at the index with the varible number, which is what was inputed
    sentence = "".join(sentence) #joins the list back into a string
    return sentence
### going to have to make multible functions to work around 
#    count_characters = len[sentence]
#test
#IGNORE ABOVE

#instead of doing 3 individual functions, im going to do one function that gets all the inputs, then another that does the replacing

STRING_A = ""
LETTER_A = ""
NUMBER_A = 0
# #attempt 2
# def grab_string_letter_number(string: str,letter: str, number: int)->str:
#     """summery
#     Discription: grabs a string, letter, and number from the user into a list.
#                 this is to be used in the the replace_in_string funtion.

#     Args:  string (str): the string to be changed
#             letter (str): the letter to be replaced
#             number (int): the index placepoint to replace the letter at in the string a for replace_in_string funtion 
#                         example: 0 = first character, 1 = second character, etc in the index of the string
#     Returns:  returns the string inputed by the user in a varible for later use

#     Note: I used no global varibles, just assighn it to a varible outside this funtion

#     """
#     string = str(input("Enter a string: "))
#     letter = str(input("Enter a letter: "))
#     number = float(input("Enter a positive number: "))
#     number = round(number)
#     number = int(number)
#     return [string, letter, number]
# string = ""
# letter = ""
# number = 0
# X = grab_string_letter_number(string, letter, number)

# def grab_script_list()
#
#  Note: I could make it work, but I dont have ennough knowlage regarding lists to make it work, so im going to do it a differnt way

#attempt 3
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



####  CODE for main funtion###
grab_string_letter_number(STRING_A, LETTER_A, NUMBER_A)
print(STRING_A, LETTER_A, NUMBER_A)





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