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


string = str(input("Enter a string: "))
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
l#ist(string) # this will make a list of the string, but it will be a list of each letter
#    for list(string) in string:


# txt = "welcome to the jungle"

# x = txt.split()

# print(x)

# print(split("welcome"))

#the replace function is a function that replaces a letter in a string at a given index
#.replace("a", "b") #replaces a with b
### This is so agrivating, I tried to turn it into a list, relpace the letter, then turn it back into a string, but if there is already a funtion that
### does that, then why would I waste my time doing that? ... I wish I know about that function before I spent 30 minutes trying to figure out how to do it