# HW4.py
# Author:

### README
# This file contains buggy functions that you need to fix.
# There are 10 buggy functions in total.
# run test.py to see which functions are buggy and what the expected output is.
# remember you can run test.py with the -v flag to see more details about the tests.
# also remember that you can run a specific test by specifying the test name after the -k flag.
# you should not change the test.py file.

# Each function has a comment above it that describes what the function should do.
# Answer each question asking where the bug is in the buggy function.
# Provide your answer as what line the bug is on and what the bug is.
# For example, if the bug is on line 5 and the bug is that the function is missing a colon, you would write:
# 5: Missing colon
# After you fix the function, you should run test.py to make sure that the function is fixed.


# REMEMBER TO play your code to save it into the memory... or you will get an error message when you run the pytest

def add(a:float, b:float) -> float:
    """Add two numbers together

    Args:
        a (float): number to add
        b (float): number to add

    Returns:
        float: the sum of a and b
    """
    return float(a) + float(b)

# Where is the bug in the buggy function?
# A:  There was a minus sign instead of a plus sign(a - b). It should be (a + b). 
#  Also there is not type enforcement for the return value,  and should be both floats.

#  error message from pytest before correction:
# >       assert add(3, 2) == 5, "Addition failed"
# E       AssertionError: Addition failed
# E       assert 1.0 == 5
# E        +  where 1.0 = add(3, 2)



def subtract(a:float, b:float) -> float:
    """Subtract two numbers

    Args:
        a (float): number to subtract from
        b (float): number to subtract

    Returns:
        float: the difference of a and b
    """
    return float(a) - float(b)
# Where is the bug in the buggy function?
# A:  There was a plus sign instead of a minus sign (a + b). It should be (a - b)
#Also there is not type enforcement for the return value,  and should be both floats.

# error message from pytest before correction:
# # E       AssertionError: Subtraction failed
# E       assert 8.0 == 2
# E        +  where 8.0 = subtract(5, 3)


def divide(a:float, b:float) -> float:
    """Divide two numbers

    Args:
        a (float): number to divide
        b (float): number to divide by

    Returns:
        float: the quotient of a and b
    """
    return float(a) / float(b)
# Where is the bug in the buggy function?
# A: there was a muliplication sign instead of a division sign(a * b). It should be (a / b). 
# while it isnt a bug,  also there is not type indent or hinting,  and it should be both floats in defining the function
# also there is not type enforcement for the return value,  and should be both floats... but it works without it.


# error message from pytest
# E       AssertionError: Division failed
# E       assert 12.0 == 3
# E        +  where 12.0 = divide(6, 2)


def multiply(a: float, b: float) -> float:
    """Multiply two numbers

    Args:
        a (float): number to multiply
        b (float): number to multiply by

    Returns:
        float: the product of a and b

        note: the pytest makes this  function fail, but it is not the only bug in this function

    """

    return float(a) * float(b)


# Where is the bug in the buggy function?
# A:  There was a division sign instead of a multiplication sign(a / b). It should be (a * b).  it was an assertion error
#Also there is not type enforcement for the return value,  and should be both floats.  


### do not put print statment in the funtion, apprently it will cause the pytest to fail,  I had to remove the print statment i accedently added to get the pytest to pass.
# error message from pytest before correction:
# E       AssertionError: Multiplication failed
# E       assert 1.3333333333333333 == 12
# E        +  where 1.3333333333333333 = multiply(4, 3)

def greet(name:str)->str:
    """Greet a person

    Args:
        name (str): name of the person to greet

    Returns:
        _type_: the greeting message
    """
    return "Hello, " + str(name) + "!"
# Where is the bug in the buggy function?
# A: there was a typo in the greeting message and the + needed to be outside of the "" marks and spaced properly.
# It should be "Hello, " + name + "!" not "Heloo, "+name+"!"
# it doesn't fail, but it should be type hinting  name in the return value, such as str(name)

# error message from pytest before correction:
# E       AssertionError: Greeting failed
# E       assert 'Heloo, John!' == 'Hello, John!'
# E         - Hello, John!
# E         ?    ^
# E         + Heloo, John!
# E         ?    ^

def square(num:int) -> int:
    """Square a number

    Args:
        num (int): number to square

    Returns:
        int: the square of the number
    """
    return int(num) * int(num)
# Where is the bug in the buggy function?
# A: It should be return num * num not return num + num.  While it doesnt fail the pytest,  it should be type hinting  num in the return value, such as int(num)

#error message from pytest before correction:
# E       AssertionError: Squaring failed
# E       assert 8 == 16
# E        +  where 8 = square(4)

def is_even(num:int) -> bool:
    """Check if a number is even

    Args:
        num (int): number to check

    Returns:
        bool: True if the number is even, False otherwise
    """
    return int(num) % 2 == 0
# Where is the bug in the buggy function?
# A: It should be return num % 2 == 0 not return num % 2 == 1. 
#  While it doesnt fail the pytest,  it should be type hinting  num in the return value, such as int(num)

# error message from pytest before correction:
# E       AssertionError: Even check failed for even number
# E       assert False == True
# E        +  where False = is_even(4)

def grade_calculator(score:float) -> str:
    """Calculate the grade based on the score

    Args:
        score (float): score to calculate the grade for

    Returns:
        str: the grade for the score
    """
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 0 <= score < 60:
        return "F"
    else:
        return "Invalid Score"
# Where is the bug in the buggy function?
# A:  elif 70 <= score < 79: should have been elif 70 <= score < 80:  it was an assertion error due to 79 left out of the calculation.
# it could have been elif 70 <= score <= 79:  but that is not how the other elif statements are written.

# error message from pytest before correction:
# E       AssertionError: Grade calculation failed for C
# E       assert 'Invalid Score' == 'C'
# E         - C
# E         + Invalid Score

def speed_check(speed:float) -> str:
    """Check if the speed is within the speed limit
    
    Args:
        speed (float): speed to check
        
    Returns:
        str: the speed check result
    """
    # Assuming general speed limits: min: 20, max: 70 (in mph)
    if speed < 20:  
        return "Too slow"
    elif 20 <= speed <= 60:
        return "Within limit"
    elif speed > 70: 
        return "Over speed limit"
    else:
        return "Unknown"
# Where is the bug in the buggy function?
# A:

# error message from pytest before correction:
# E       AssertionError: Speed check failed for upper end of within limit
# E       assert 'Unknown' == 'Within limit'
# E         - Within limit
# E         + Unknown

def is_leap_year(year:int) -> bool:
    """Check if a year is a leap year

    Args:
        year (int): year to check

    Returns:
        bool: True if the year is a leap year, False otherwise
    """
    if year % 4 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 400 == 0:
        return True
    else:
        return False
# Where is the bug in the buggy function?
# A:

# error message from pytest before correction:
# E       AssertionError: Leap year check failed for century non-leap year
# E       assert True == False
# E        +  where True = is_leap_year(1900)
def main():
    print("You are running me directly!")

if __name__ == "__main__":
    main()


"""import os

os.chdir('/path/to/new/directory')"""

""" how to pytest





"""