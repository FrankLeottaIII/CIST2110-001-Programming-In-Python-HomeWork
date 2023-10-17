#HW3TroubleshootingHW3.py
"""
Question 2
string = str(input("Enter a string: "))
letter = str(input("Enter a letter: "))
number = float(input("Enter a number: "))
number = round(number)
number = int(number)

len(string-number)


readlines()"""

#getting info from vid Thur October 5th | Bank Account Program and Project 1
#5:31

#split is a function that splits a string into a list where each word is a list item
# slice is a function that takes a string and returns a string with the first letter capitalized
# len is a function that returns the length of a string
# replace is a function that replaces a letter in a string at a given index
# isdigit is a function that returns true if a string is a number
# isalpha is a function that returns true if a string is a letter
# isalnum is a function that returns true if a string is a letter or number
# islower is a function that returns true if a string is lowercase
# isupper is a function that returns true if a string is uppercase
# lower is a function that returns a string with all letters lowercase
# upper is a function that returns a string with all letters uppercase
# title is a function that returns a string with the first letter of each word capitalized
# splitlines is a function that splits a string into a list where each line is a list item
# join is a function that takes a list of strings and joins them together


# string = str(input("Enter a string: "))
# letter = str(input("Enter a letter: "))
# number = float(input("Enter a number: "))
# number = round(number)
# number = int(number)
# len(count) wrong, it will be the length of the string, not the index of the string
#list(count) no and dont import re to make every eltter in a list, and get rid of one letter #copilot: and use re.split... what?
#len(string-number) #IS WRONG

# after each letter add a space, then remove the space at the index Wrong
# string = string + " "Wrong
#string = <string>.join(string.split(" "))  Wrong
#list(string) # this will make a list of the string, but it will be a list of each letter
#    for list(string) in string:


# txt = "welcome to the jungle"

# x = txt.split()

# print(x)

# print(split("welcome"))

#the replace function is a function that replaces a letter in a string at a given index
#.replace("a", "b") #replaces a with b
### This is so agrivating, I tried to turn it into a list, relpace the letter, then turn it back into a string, but if there is already a funtion that
### does that, then why would I waste my time doing that? ... I wish I know about that function before I spent 30 minutes trying to figure out how to do it

## trying something else now

sentence = str(input("Enter a string: "))
letter = str(input("Enter a letter: "))
number = float(input("Enter a number: "))
number = round(number)
number = int(number)
# len(count) wrong, it will be the length of the string, not the index of the string
#list(count) no and dont import re to make every eltter in a list, and get rid of one letter #copilot: and use re.split... what?
#len(string-number) #IS WRONG

# after each letter add a space, then remove the space at the index Wrong
# string = string + " "Wrong
#string = <string>.join(string.split(" "))  Wrong
#ist(string) # this will make a list of the string, but it will be a list of each letter
#    for list(string) in string:

#string = string.replace(letter, str(number)) not working either
# #for list(string) in string: #SyntaxError: cannot assign to function call
# for number in string:
#     if string == number:
#         string = letter
# print(string)

#Trying something new now
""" actually works, just need to combine list
sentence= list(sentence)
len(sentence)
#if  letter == string[number] ignoring " " is how I need to do it, but I dont know how to do that... but it didnt ask for in the question so I wont do it
sentence[number] = letter
print(sentence)
"""
## idiotproofed it, but this is the wrong code, dont want to save it due to copilot wanting to give me my mistakes as the answer lol
##in essence,  I need to make sure the number is not larger than the string, but Its best to leave it to numbers
"""Wrong way of coding, this code is not working
# while checking < number == True:    #remember while loops need 2 exits, one for true and one for false
#     print("The number you inputed is larger than the string you inputed, please try again")
#     number = float(input("Enter a number. It will be rounded: "))
#     number = round(number)
#     number = int(number)
#     if checking > number == False:
#         continue
#     while IndexError:
#         print("The number you inputed is larger than the string you inputed (b), please try again")
#         number = float(input("Enter a number. It will be rounded: "))
#         number = round(number)
#         number = int(number)
#         if not IndexError:
#             break
it would just loop indefinatly

"""

##Troubleshooting HW3

"""
This is a repository of all the troubleshooting I did for HW3
to get rid of clutter in the main file.

"""

#PROBLEM 1

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

###question 2
# IE. If the user inputs "Hello World", "a", and 3, the function should return "Helao World"
#
#def replace(string:str, letter:str, number:int)->str: """ did not need these varibles,  this is for a differnt use"""


#attempt 1

# def replace_in_string()->str:
#     """summery
#     Discription: replaces a letter in a string, any floats will be rounded to the nearest whole number

#     Args:  string (str): the string to be changed

#     Returns:  str: the string with the letter replaced
#     """
#     sentence = str(input("Enter a string: "))
#     letter = str(input("Enter a letter: "))
#     number = float(input("Enter a positive number: "))
#     number = round(number)
#     number = int(number)
#     sentence= list(sentence)
#     count_characters = len[sentence]
#     count_characters = int(count_characters)
#     if count_characters < number:
#         print("The number you inputed is larger than the string you inputed, please try again")
#         replace_in_string(sentence, letter, number)
#     len(sentence)
#     sentence[number] = letter  #replaces the letter at the index with the varible number, which is what was inputed
#     sentence = "".join(sentence) #joins the list back into a string
#     return sentence
### going to have to make multible functions to work around 
#    count_characters = len[sentence]
#test
#IGNORE ABOVE

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







#instead of doing 3 individual functions, im going to do one function that gets all the inputs, then another that does the replacing

# STRING_A = ""
# LETTER_A = ""
# NUMBER_A = 0
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
# def str_to_list(varible: str)->list:
#     """summery
#     Discription: converts a string into a list

#     Args:  varible (str): the string to be changed

#     Returns:  list: the string converted into a list

#     Note: I used no global varibles, just assighn it to a varible outside this funtion

#     """
#     varible.split()
#     return  varible.split()

# STRING_A = " HELLO WORLD... AGAIN"
# STRING_A = str_to_list(STRING_A)
# print(STRING_A)
# needs to be list, not indivdual words


#test it


#         print("The number you inputed is larger than the string you inputed, please try again")
#         replace_in_string(sentence, letter, number)
#     len(sentence)
#     sentence[number] = letter  #replaces the letter at the index with the varible number, which is what was inputed
#     sentence = "".join(sentence) #joins the list back into a string
#     return sentence





