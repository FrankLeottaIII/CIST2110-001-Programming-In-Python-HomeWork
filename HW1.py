# HW1.py
# Author: Frank R. Leotta III

# Question 1:
# Print Hello World like we did in class
print("Hello World!")
# Question 2:
# Print the following:
# Your name
print("Frank R. Leotta III")
# Your age
print("34")
# Your favorite color
print("green")   
# Your favorite animal
print("axolotl")
# Question 3:
# Create a variable called "myName" and set it equal to your name
myName = "Frank R. Leotta III"
# Create a variable called "myAge" and set it equal to your age
myAge = "34"
# Create a variable called "myColor" and set it equal to your favorite color
myColor = "green"
# Create a variable called "myAnimal" and set it equal to your favorite animal
myAnimal = "axolotl"
# Print the following:
# Hello, my name is <myName>
print("Hello, my name is " + myName)
# I am <myAge> years old
print("I am " + myAge + " years old")
# My favorite color is <myColor>
print("My favorite color is " + myColor)
# My favorite animal is <myAnimal>
print("My favorite animal is " + myAnimal)

# Question 4:
# Calculate the following and print the result:
# 2 + 2
print(2 + 2)
# 3 * 4
print(3 * 4)
# 5 - 6
print(5 - 6)
# 8 / 2
print(8 / 2)
# Question 5:
# Create a variable called "num1" and set it equal to 2
num1 = 2
# Create a variable called "num2" and set it equal to 3
num2 = 3
# Create a variable called "num3" and set it equal to 4
num3 = 4
# Create a variable called "num4" and set it equal to 5
num4 = 5
# Calculate the following and print the result:
# num1 + num2
print(num1 + num2)
# num3 * num4
print(num3 * num4)
# num4 - num1
print(num4 - num1)
# num2 / num1
print(num2 / num1)  
# Question 6: Write a program that asks the user for their name and then prints the following:

# Hello, <name>. Please enter three numbers.
name_of_user =  input("hello, Please enter your name:") 
# The program should then ask the user for three numbers (floats) and print the following:
first_number = float(input("ok. Now I need a 3 numbers, please enter the first number: "))
second_number = float(input("Please enter the second number next: "))
third_number = float(input("Ok nice.  Please enter the third number: "))

# 1. The sum of the three numbers is <sum>
print("The sum of the three numbers is " + str(first_number + second_number + third_number))
# 2. The product of the three numbers is <product>
print("The product of the three numbers is " + str(first_number * second_number * third_number))
# 3. round the three numbers to the nearest integer and print the sum of the three rounded numbers divided by 3 
print("let me add them up and then round it to the nearest interger for you, beep boop...")

print("the sum of the 3 numbers, rounded to the nearest integer is " + str(round(first_number + second_number + third_number, 0)))
# 4. The average of the three numbers is <average>
add_tree = int(round(first_number + second_number + third_number, 0))


print("Also, the average of those three numbers is " + str(round(add_tree/3)) + ", rounded to the nearest integer")    
# Question 7: Ask the user for an input of a symbol (in the example its *)     
# Print a diamond of the symbol that looks like the following. Include the spaces and the | character. 
# Hint: the print("symbol", end="") with \t and \n characters will be useful here.

#    *     |
#   ***    |
#  *****   |
# *******  |
#  *****   |
#   ***    |
#    *     |
print("Thank you") 
s = input("Before you go, I would now like to draw 2 diamonds for you.  Please enter a symbol you would like to use: ")
print("ok here are the 2 dimonds for your time, have a wonderful day!!!")

print("    " + s + "     |")
print("   " + s + s + s + "    |")
print("  "+s + s + s + s + s + "   |")
print(" "+ s + s + s + s + s + s + s + "  |")
print("  "+ s + s + s + s + s + "   |")
print("   " + s + s + s + "    |")
print("    "+ s + "     |")
print(" ")
print("    " + s, end = "     |\n")
print("   " + s + s + s, end =  "    |\n")
print("  "+s + s + s + s + s, end = "   |\n")
print(" "+ s + s + s + s + s + s + s, end = "  |\n")
print("  "+ s + s + s + s + s, end = "   |\n")
print("   " + s + s + s, end = "    |\n")
print("    "+ s, end = "     |\n")
end = ("\n")