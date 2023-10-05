# HW2.py
# Author: Frank R. Leotta III


# Question 1:
# Write some code that prompts the user for their age. Depending on the input:
age = int(input("Enter your age: "))

# If the age is less than 13, print "You are a child."
if age < 13:
    print("You are a child.")
# If the age is between 13 and 19, print "You are a teenager."
elif age >= 13 and age <= 19:
    print("You are a teenager.")
# If the age is 20 or older, print "You are an adult."
elif age >= 20:
    print("You are an adult.")

# Question 2:
# Write some code to display the following pattern using a for or while loop:
# 1
# 12
# 123
# 1234
# 12345

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end = "")
    print()
# So first is J what you want to do, then i is how many times you want to do it... its odd and confusing
# but it works... sometimes you need break it into chunks to understand it
# written
# #end = "" needed or it would be on a new number
# remember to print() at the end of the loop to make it go to the next line


# Question 3:
# Write a Python program that prompts the user to input 10 numbers. After all the numbers are inputted, the program should display:

# The highest number.
# The lowest number.
# The average of all the numbers.
def ask_for_number():
    number = float(input("Please enter a number I will ask you 10 times for each : "))
    return number

one = ask_for_number()
two = ask_for_number()
three = ask_for_number()
four = ask_for_number()
five = ask_for_number()
six = ask_for_number()
seven = ask_for_number()
eight = ask_for_number()
nine = ask_for_number()
ten = ask_for_number()

print("The highest number is: " + str(max(one, two, three, four, five, six, seven, eight, nine, ten)))
print("The lowest number is: " + str(min(one, two, three, four, five, six, seven, eight, nine, ten)))
print("The average of all the numbers is: " + str((one + two + three + four + five + six + seven + eight + nine + ten) / 10))

#I wonder if you could have made a varible for varibles in min and max.  if you could deconstruct a list into varibles

# Question 4:
# Vowel Counter - Write some code that prompts the user to enter a string. The program should then display the number of vowels in the string. IE. If the user enters "Hello World", the program should display 3.
# the vowels are a, e, i, o, u
# Hint: convert the string to lowercase and use a for loop with a counter variable and an if statement

counter = input("Please enter a string, I will count the vowels: ")
counter = counter.lower()
vowel_count = 0 
for i in counter:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowel_count += 1
print("There are " + str(vowel_count) + " vowels in your string")
    