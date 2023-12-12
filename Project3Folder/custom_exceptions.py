# makeing custom exceptions

#use word wrap for this file

#In Python, you can create a custom exception by defining a new class that inherits from the built-in Exception class. Here's an example:

class CustomException(Exception):
    def __init__(self, message):
        self.message = message

#Now, you can raise your custom exception like this:

#raise CustomException("An error occurred")

#example of custom exception use
def add_user(self, user: User):
    if not isinstance(user, User):
        raise CustomException("Invalid user type")
    self.users.append(user)

#Now, if you try to add something other than a User object to the users list, you'll get an error message like this:

#Traceback (most recent call last):
#  File "main.py", line 10, in <module>
#    library.add_user("John Doe")
#  File "main.py", line 6, in add_user
#    raise CustomException("Invalid user type")
#########################################
class CustomException(Exception):
    def __init__(self, message):
        self.message = message
#
# Usage:
try:
    raise CustomException("This is a custom exception message")
# In this code, CustomException is a new class that inherits from the built-in Exception class. The __init__ method is a special method that gets called when you create a new instance of the class. This method takes a message parameter and assigns it to the message attribute of the class.

# Then, when you raise this exception in your code, you can pass a string to the constructor to set the message:
