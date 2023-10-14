# HW3.py
# Author: Frank R. Leotta III

# This Homework assignment is meant to test your ability to make functions within python as well as importing and using modules. This assignment might require you to do some research on your own. If you get stuck, try googling the problem, especially when it comes to importing and using the different modules.

# Question 1:
# Write a function that takes in a number and returns that number squared
# IE. If the user inputs 3, the function should return 9"""

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
def replace(string:str, letter:str, number:int)->str:
    """summery
    Discription: replaces a letter in a string, any floats will be rounded to the nearest whole number

    Args:   string (str): the string to be changed
            letter (str): the letter to be replaced
            number (int): the index to replace the letter at

    Returns:  str: the string with the letter replaced
    """
    sentence = str(input("Enter a string: "))
    letter = str(input("Enter a letter: "))
    number = float(input("Enter a number: "))
    number = round(number)
    number = int(number)
    sentence= list(sentence)
    if len[sentence] < number:
        print("The number you inputed is larger than the string you inputed, please try again")
        replace(string, letter, number)
    len(sentence)
    sentence[number] = letter  #replaces the letter at the index with the varible number, which is what was inputed
    sentence = "".join(sentence) #joins the list back into a string
    print(sentence)

  
    sentence = str(input("Enter a string: "))
    letter = str(input("Enter a letter: "))
    number = float(input("Enter a number: "))
    number = round(number)
    number = int(number)
    sentence= list(sentence)
    if len[sentence] < number:
        print("The number you inputed is larger than the string you inputed, please try again")
        replace(string, letter, number)
    len(sentence)
    sentence[number] = letter  #replaces the letter at the index with the varible number, which is what was inputed
    sentence = "".join(sentence) #joins the list back into a string
    print(sentence)



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

# Question 5:
# import the random module and use it to generate a random number between 1 and 100

# Question 6:
# import the math module and use it to find the square root of 16 (hint: use the sqrt() function)

# Question 7:
# import the sys module and use it to display the version of python you are using
# this time import the module using the import "as" keyword
# hint: use the version attribute (sys.version)

# Question 8:
# import the os module and use it to display the current working directory. This time import the module using the from keyword
# hint: use the getcwd() function
