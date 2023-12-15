#  ________  ________  ________        ___  _______   ________ _________        ________
# |\   __  \|\   __  \|\   __  \      |\  \|\  ___ \ |\   ____\\___   ___\     |\_____  \
# \ \  \|\  \ \  \|\  \ \  \|\  \     \ \  \ \   __/|\ \  \___\|___ \  \_|     \|____|\ /_
#  \ \   ____\ \   _  _\ \  \\\  \  __ \ \  \ \  \_|/_\ \  \       \ \  \            \|\  \
#   \ \  \___|\ \  \\  \\ \  \\\  \|\  \\_\  \ \  \_|\ \ \  \____   \ \  \          __\_\  \
#    \ \__\    \ \__\\ _\\ \_______\ \________\ \_______\ \_______\  \ \__\        |\_______\
#     \|__|     \|__|\|__|\|_______|\|________|\|_______|\|_______|   \|__|        \|_______|
# Author:Frank Robert Leotta III
# CIST2110-001-Project-3 Library Management System (LMS)
# Project 3 will implement a library management system (LMS) that will allow users to manage books, users, and a library to manage collection of books and users.
# The LMS will be menu driven and will allow users to add, delete, and update books and users.
# Users will also be able to borrow and return books.
# The LMS will also allow users to search for books and users.

# ENABLE WORD WRAP TO MAKE THINGS EASIER TO READ:
# VIEW (at the top) -> WORD WRAP

# Import statements:
import csv
# Project outline and requirements:

# OUTLINE - The LMS will consist of the following classes and methods:

# 1. Create a Book class that has the following attributes (create a __init__ method)):
#    a. isbn (int)
#    b. title (string)
#    c. author (string)
#    d. borrowed (boolean) - this should not be passed in as a parameter, it should be set to False by default
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES
class Book:
    def __init__(self, title: str, author: str, isbn: int) -> None:
        """
        Initializes a Book object with the given attributes: isbn, title, and author.
        The borrowed attribute is set to False by default.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (int): The ISBN of the book.
        Returns:
            None
        """
        self.title: str = title
        self.author: str = author
        self.isbn: int = isbn
        self.borrowed: bool = False
# Methods:
#    a. __str__ (returns a string representation of the book using the following format: ISBN: <ISBN>, Title: <Title>, Author: <Author>, Borrowed: <Borrowed>)
    def __str__(self)-> str:
        """Summery:
            Returns a string representation of the book using the following format: ISBN: <ISBN>, Title: <Title>, Author: <Author>, Borrowed: <Borrowed>.  

            Args:
                None
            
            Returns:
                str: The string representation of the book.
                None: If any error is raised.
        """
        try:
            return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Borrowed: {self.borrowed}"
        except Exception as e:
            print("looks like that book is purely imaginary...")
            print(f"its either that or {e} is the problem...")
#    b. check_out - sets borrowed to True and returns a message that the book has been checked out
    def check_out(self)->str: #says check_out in pytest, fixing it...
        """Summery:
        
        Sets the borrowed attribute to True and returns a message that the book has been checked out.  The code is encapsulated in a try except block format.  If any error is raised, the function questions its sanity and wonders about if it saw one of schrodinger's cats or if it was the error that was raised. In this state, the method returns None.
        
        Args:
            None
            
            Returns:
                str: A message that the book has been checked out.
                None: If any error is raised.
                """
        try:
            self.borrowed = True
            return f"the book has been checked out"
        except Exception as e:
            print("...what")
            print(f"Was it on of my roomates cats or the error: {e} that broke me?")

#    c. check_in - sets borrowed to False and returns a message that the book has been checked in
    def check_in(self)->str:
        """Summery:
        Sets the borrowed attribute to False and returns a message that the book has been checked in.  The code is encapsulated in a try except block format.  If any error is raised, the function smiles and does not check in the users book... it just stares at the user and gives nothing to the user.
        Args:
            None
            
            Returns:
                str: A message that the book has been checked in.
                None: If any error is raised."""
        try:
            self.borrowed = False
            return f"the book has been checked in"
        except Exception as e:
            print(":)")
            print("...")

        return f"Book has been checked in"
#    d. borrowed - returns True if the book is borrowed and False if the book is not borrowed
    def borrowed(self)->bool: 
        """Summery:
        This method is used to check to see if a book is borrowed or not. 
        If it is borrowed, it returns True and if it is not borrowed, it returns False.
        The borrowed attribute is set to False by default.
        The code is encapsulated in a try except block format.  If any error is raised, the function becomes catotonic giving out nothing to the user.
        
        Args:
            None
            
            Returns:
                bool: True if the book is borrowed, False if the book is not borrowed
                None: If any error is raised."""
        try:
            if self.borrowed == True:
                return True
            else:
                return False
        except Exception as e: 
            print("...")
            



# 2. Create a User class that has the following attributes (create a __init__ method)):
#    a. name (string)
#    c. member_id (int)
#    d. borrowed_books (list of books) - this should not be passed in as a parameter, it should be set to an empty list by default
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES
class User:
    def __init__(self: str, name: int, member_id: int)-> None: #says member_id in pytest instead of ID, fixing it...
        """Summery:
            Initializes a User object with the given attributes: name, and member_id.
            The borrowed_books attribute is set to an empty list by default.  The code is encapsulated in a try except block format.  If any error is raised, the function is horrified at the user's actions and informs the user that they broke the user class's soul. They then inform the user that the error is a extreame sin in some Religions.

            Args:
                name (str): The name of the user.
                member_id (int): The ID of the user.
            
            Returns:
                None
        """
        try:
            self.name: str = name
            self.member_id: int = member_id
            self.borrowed_books: list = []
        except Exception as e:
            print("Holy crap this is bad...  You broke the user class... the soul of the object...  You monster.")
            print(f"I am sure that {e}is consitered a extreame sin in some Religions.")

# Methods:
#    a. __str__ (returns a string representation of the user using the following format: Name: <Name>, ID: <ID>, Borrowed Books: <Borrowed Books>)
    def __str__(self)-> str:
        """Summery:
            Returns a string representation of the user using the following format: Name: <Name>, ID: <ID>, Borrowed Books: <Borrowed Books>.  This is a User class exclusive method.  The code is encapsulated in a try except block format.  If any error is raised, the function is horrified at the user's actions and informs the user that they broke the user class.  They then inform the user that the error is a war crime in some countries.

            Args:
                None
            
            Returns:
                str: The string representation of the user.
                None: If any error is raised.
                """
        try:
            return f"Name: {self.name}, ID: {self.member_id}, Borrowed Books: {self.borrowed_books}"
        except Exception as e:
            print("Holy crap this is bad...  You broke the user class.")
            print(f"I am sure that {e}is consitered a war crime in some countries.")

#    b. borrow_book - adds the book to the borrowed_books list, updates the borrowed attribute of the book to True, and returns a message that the book has been checked out (should take a book as a parameter)
    def borrow_book(self, book: Book)-> str:
        """Summery:
            Adds the book to the borrowed_books list, updates the borrowed attribute of the book to True, and returns a message that the book has been checked out.  the code is encapsulated in a try except block format.  If any error is raised, the user is informed that cannot check out the book and is informed what is preventing the checkout.

            Args:
                book (Book): The book object to add to the borrowed_books list.

            Returns:
                str: A message that the book has been checked out.
                None: If any error is raised.
                """
        try:
            self.borrowed_books.append(book)
            book.check_out()
            return print("The book has been checked out")
        except Exception as e:
            print("You should put that back... can't check you out right now")
            print(f"this is what is preventing the checkout: {e}")

        
#    c. return_book - removes the book from the borrowedBooks list, updates the borrowed attribute of the book to False, and returns a message that the book has been checked in (should take a book as a parameter)
    def return_book(self, book: Book)-> str:
        """Summery:
            Removes the book from the borrowed_books list, updates the borrowed attribute of the book to False, and returns a message that the book has been checked in.  This method is exclusive to the User class.  The code is encapsulated in a try except block format.  If any error is raised, the user is informed that they are not going to return the book without pity, and informed what broke it.

            Args:
                book (Book): The book object to remove from the borrowed_books list.

            Returns:
                str: A message that the book has been checked in.
                None: If any error is raised.
                """
        try:
            self.borrowed_books.remove(book)
            book.check_in()
            return print("The book has been checked in")
        except Exception as e:
            print("looks like your not returning that book... sucks to be you.")
            print(f"this is what broke it: {e}")


# 3. Create a Library class that has the following attributes (create a __init__ method)):
#    a. books (list of books)
#    b. users (list of users)

# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES
class Library:
    def __init__(self)-> None:
        """ Summery:
            Initializes a Library object with the following attributes: books and users.  The books and users attributes are set to empty lists by default.  This is a Library class exclusive method.  The code is encapsulated in a try except block format.  If any error is raised, the user is informed that they messed up in a spectacularly impressive way, then informed of the type of error that was raised.... then waits patiently in silence.

            Args:
                None
            
            Returns:
                None
        """
        try:
            self.books: list = []
            self.users: list = []
        except Exception as e:
            print(f"wow thats impressive.  You somehow caused this error to occur: {e}")
            print("...")

# Methods:
#    a. __str__ (returns a string representation of the library using the following format: Books: <Books>, Users: <Users>)
    def __str__(self)-> str:
        """Summery:
            Returns a string representation of the library using the following format: Books: <Books>, Users: <Users>  This is a Library class exclusive method.  The code is encapsulated in a try except block format.  If any error is raised, the user is informed that there is a problem and is informed what error it is while waiting patiently for the user to fix the problem... then returns None.

            Args:
                None
            
            Returns:
                str: The string representation of the library.
                none: If any error is raised.
        """
        try:
            return f"Books: {self.books}, Users: {self.users}"
        except Exception as e:
            print("An error has occured.")
            print(e)
            print("...")
#    b. add_book - adds a book to the books list (should take a book as a parameter)
    def add_book(self, book: Book)-> None:
        """Summery:
            Adds a book to the books list.  A book object is passed in as a parameter.  This method does not return anything. This method is exclusive to the Library class.  the code is encapsulated in a try except block format.  If any error is raised, the user is informed that there is a problem and is informed what error it is while waiting patiently for the user to fix the problem.

            Args:
                book (Book): The book object to add to the books list.

            Returns:
                None
            """
        try:
            self.books.append(book)
        except Exception as e:
            print("An error has occured.")
            print(e)
            print("...")

#    c. add_user - adds a user to the users list (should take a user as a parameter)
    def add_user(self, user: User)-> None:
        """Summery:
            Adds a user to the users list.  A user object is passed in as a parameter.  This method does not return anything. This method is exclusive to the Library class.  The code is encapsulated in a try except block format.  If any error is raised, the user is informed that there is a problem and is informed what error it is while waiting patiently for the user to fix the problem.

            Args:
                user (User): The user object to add to the users list.

            Returns:
                None
            """
        try:
            self.users.append(user)
        except Exception as e:
            print("An error has occured.")
            print(e)
            print("...")

#    d. find_book - returns the book with the given ISBN (should take an ISBN as a parameter)
    def find_book(self, isbn: int) -> Book:
        """
            Find a book by its ISBN.   This method takes an ISBN as a parameter. This method searches the book list to see if the paramiter ISBN matches the isbn in the book list.   It returns the book object if found, None otherwise.
            The code is encapsulated in a try except block format.  If any error is raised, the user is informed that there is a problem and thinks about what went wrong... but doesn't tell the user.

        Args:
            isbn (int): The ISBN of the book to find.

        Returns:
            Book: The book object if found, or None otherwise.

        """
        try:
            for book in self.books:
                if book.isbn == isbn:
                    return book
                return None
        except Exception as e:
            print("An error has occured.  Please contact the developer.")
            print("hmmmm...")
  

#    e. find_user - returns the user with the given ID (should take an ID as a parameter)
    def find_user(self, member_id: int) -> User:
        """
        Find a user by their ID. This method takes an ID as a parameter. This method searches the user list to see if the parameter ID matches the ID in the user list. It returns the user object if found, None otherwise.  The code is encapsulated in a try except block format.  If any error is raised, the user is informed that there is a problem and gives the user an attitude.

        Args:
            member_id (int): The ID of the user to find.

        Returns:
            User: The user object if found, None otherwise.
        """
        try:
            for user in self.users:
                if user.member_id == member_id:
                    return user
                return None
        except Exception as e:
            print("An error has occured.  Please contact the developer.")
            print("whatever...")
 
#    f. export_books_to_csv - exports the books list to a csv file (should take a filename as a parameter)
#       The csv file should have the following format: ISBN,Title,Author,Borrowed
#       The csv.DictWriter class is very useful for this: https://docs.python.org/3/library/csv.html#csv.DictWriter
    def export_books_to_csv(self, filename: str)-> None:
        """
        Export the books list to a csv file. The csv file should have the following format: ISBN,Title,Author,Borrowed.
          If the book is borrowed, the borrowed attribute is exported as True. If the book is not borrowed, the borrowed attribute is 
          exported as False.
        The code is encapsulated in a try except block format.  If a FileNotFoundError, or any other error is raised, the user is informed that there is a problem and apologizes.

        Args:
            filename (str): The name of the file to export to.

        Returns:
            None
        """
        try:
            with open(filename, "w", encoding='utf-8', newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["ISBN", "Title", "Author", "Borrowed"])
                writer.writeheader()
                for book in self.books:
                    writer.writerow({"ISBN": book.isbn, "Title": book.title, "Author": book.author, "Borrowed": book.borrowed})
        except FileNotFoundError:
            print(" this should not happen... if you see this, please contact the developer.")
            print("File not found")
        except Exception as e:
            print("An error has occured.  Please contact the developer.")
            print("sorry")


#    g. export_users_to_csv - exports the users list to a csv file (should take a filename as a parameter)
#       This will be similar to the export_books_to_csv method but there is a slight difference with the borrowedBooks attribute if you get stuck this code might help:
#       borrowed_books_titles = [book.title for book in user.borrowed_books]
#       Use that and pythons .join method to create a string of the borrowed books titles
    def export_users_to_csv(self, filename)-> None:
        """
        Export the users list to a csv file.  if the user has borrowed books, the borrowed books titles are exported as a string. If the user has not borrowed any books, the borrowed books titles are exported as an empty string. The csv file should have the following format: Name,ID,Borrowed Books. The code is encapsulated in a try except block format.  If a TypeError, FileNotFoundError, or any other error is raised, the user is informed that there is a problem and patiently waits there silently.

        Args:
            filename (str): The name of the file to export to.

        Returns:
            None
        """
        try:
            with open(filename, "w", encoding='utf-8', newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "ID", "Borrowed Books"])
                for user in self.users:
                    borrowed_books_titles = [book.title for book in user.borrowed_books]
                    writer.writerow([user.name, user.member_id, ", ".join(borrowed_books_titles)])
        except FileNotFoundError:
            print(" this should not happen... if you see this, please contact the developer.")
            print("File not found")
        except TypeError:
            print(" Problem with the type of data being exported.  Please contact the developer.")
            print("...")
        except Exception as e:
            print("An error has occured.  Please contact the developer.")
            print("....")


# 4. Create a menu that will allow users to:
#    a. Add books
#    b. Add users
#    c. Delete books
#    d. Delete users
#    g. Borrow books
#    h. Return books
#    i. Search books
#    j. Check if book is available
#    k. Search users
#    l. Export books to csv
#    m. Export users to csv
#    z. Exit
choice = ""
def menu()-> str:
    """Summary:
        Lists the menu options for the user to choose from.  The user chooses an option and if the option is valid, the user's choice is returned.    If the option is invalid due to the input not being in the c, the user is asked to choose again, using a while loop.  A list called choice_list  is used to determin if the option is invalid or not.  The choice_list will have all the options in the menu  The user's choice is returned when a valid option is chosen, breaking the while loop.  The code is encapsulated in a try except block to handle errors.  The ValueError, UnboundLocalError, TypeError, AttributeError, IndexError, and KeyError exceptions are the exact same way as if it was running normally but informing the users of the errors.  Most of the Exceptions will not really be nessary, but it looks impressive.  If any other errors are raised, the code will act the same way as the non raised code. This function is used to call the appropriate methods and can under no cercumstances be broken, or the program will be utterly useless, and I bet some people will be mad at you for that.
        Args:
            None
        
        Returns:
            choice (str): The user's choice from the menu.
            choice (str): If ValueError is raised.
            choice (str): If UnboundLocalError is raised.
            choice (str): If TypeError is raised.
            choice (str): If AttributeError is raised.
            choice (str): If IndexError is raised.
            choice (str): If KeyError is raised.
            choice (str): If any other error is raised.
    
    """
    global choice
    try:
        print("Welcome to the Library Management System!")
        print("Please choose an option from the menu below:")
        print("Press 1 to Add books")
        print("Press 2 to Add users")
        print("Press 3 to Delete books")
        print("Press 4 to Delete users")
        print("Press 5 to Borrow books")
        print("Press 6 to Return books")
        print("Press 7 to Search books")
        print("Press 8 to Check if book is available")
        print("Press 9 to Search users")
        print("Press 10 to Export books to csv")
        print("Press 11 to Export users to csv")
        print("Press 12 to Exit")
        choice = input("Enter your choice: ")
        choice_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12", "restart"]
        while choice not in choice_list:
            choice = input("Error.  Please enter a valid option from the menu: ")
        return choice
    except ValueError:
        choice = input("ValueError.  Please enter a valid option from the menu: ")
        choice_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12" "restart"]
        while choice not in choice_list:
            choice = input("Error.  Please enter a valid option from the menu: ")
        return choice
    except UnboundLocalError:
            print("UnboundLocalError.  Please enter a valid option from the menu: ")
            choice_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12", "restart"]
            while choice not in choice_list:
                choice = input("Error.  Please enter a valid option from the menu: ")
            return choice
    except TypeError:
        choice = str(input("TypeError.  Please enter a valid option from the menu: "))
        choice_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12", "restart"]    
        while choice not in choice_list:
            choice = input("Error.  Please enter a valid option from the menu: ")
        return choice
    except AttributeError:
        choice = input("AttributeError.  Please enter a valid option from the menu: ")
        choice_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12", "restart"]
        while choice not in choice_list:
            choice = input("Error.  Please enter a valid option from the menu: ")
        return choice
    except IndexError:
        choice = input("IndexError.  Please enter a valid option from the menu: ")
        choice_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12", "restart"]
        while choice not in choice_list:
            choice = input("Error.  Please enter a valid option from the menu: ")
        return choice
    except KeyError:
        choice = input("KeyError.  Please enter a valid option from the menu: ")
        choice_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12", "restart"]
        while choice not in choice_list:
            choice = input("Error.  Please enter a valid option from the menu: ")
        return choice
    except Exception as e:
        choice = input("Exception.  Please enter a valid option from the menu: ")
        choice_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12", "restart"]
        while choice not in choice_list:
            choice = input("Error.  Please enter a valid option from the menu: ")
        return choice
# RQUIREMENTS:
# 1. You should be doing error checking on all user input (make sure the user enters a valid ISBN, ID, etc.) and handle any errors appropriately (i.e. if the user enters an invalid ISBN, ask them to enter a valid ISBN)
# 2. You should be using try except blocks to handle any errors
# 3. You should be using the classes and methods outlined above with the exact names and parameters
# 4. You should be using the menu to call the appropriate methods
# 5. There is a Project3Tests.py file that will help you test your code. You should be able to run that file and pass all the tests.
#    Remember to run pytest use the following command in the terminal: pytest Project3Tests.py
# 6. The Project3Tests.py file is missing 2 tests. test_user_return and test_library_find_user. You will need to implement those tests and ensure they pass.
# 7. In your main method you should create a library object first to use for the rest of the program. You should not be creating a new library object every time you call a method. (Similar to the Store object in Lab 11)
# 8. In your main method you should be using a while loop to keep the program running until the user chooses to exit.

# IMPORTANT: You will only have 1 submission for this project so make sure you test your code thoroughly before submitting.

##user return... 

# You will be graded on the following:
# 1. Did you follow the project outline and requirements?
# 2. Does your code run without errors?
# 3. Did you use try except blocks to handle errors?
# 4. Did you use the classes and methods outlined above with the exact names and parameters?
# 5. Did you use the menu to call the appropriate methods?
# 6. Did you include docstrings for all classes and methods?
# 7. Did you include type hints for all methods?
# 8. Did your pytests for the test_user_return and test_library_find_user work?

#do you wish to continue question funtion
def continue_question()-> bool:
    """Summary:
        Asks the user if they want to continue using the program.  If the user enters y or Y, the program continues, and returns True.  If the user enters n or N, the user is informed they are going to catapulted back to the main menu.  The user is returned to the main menu, and returns False  If the user enters anything else, the program asks the user to enter yes or no, using the question_list list to determin if the input is valid.  The code is encapsulated in a try except block to handle errors.
        If ValueError, UnboundLocalError, TypeError or any other error is raised, the funtion will not keep their composure and become histerical. They will then inform the user they will be catapulted to the main menu... and then returns false.

        Args:
            None
        
        Returns:
            True: If the user enters y or Y.
            False: If the user enters n or N.
            False: If ValueError is raised.
            False: If UnboundLocalError is raised.
            False: If TypeError is raised.
            False: If any other error is raised.
    """

    print("Do you wish to continue?")
    print ("Enter y or Y for yes")
    print ("Enter n or N for no")
    try:
        question_list = ["y", "Y", "n", "N"]
        question = input("Enter your choice: ")
        while question not in question_list:
            question = input("Error.  Please enter y for yes or n for no: ")
        if question == "y" or question == "Y":
            return True
        elif question == "n" or question == "N":
            print("Ok, you will be catapulted back to the main menu.")
            return False
    except ValueError:
        print("Ok, you will be catapulted back to the main menu.")
        return False
    except UnboundLocalError:
        print("Ok, you will be catapulted back to the main menu.")
        return False
    except TypeError:
        print("Ok, you will be catapulted back to the main menu.")
        return False
    except Exception as e:
        print("Ok, you will be catapulted back to the main menu.")
        return False
#Methods to use for correct input from user:

def imput_isbn()-> int:
    """Summary:
        Asks the user to enter an ISBN. If the ISBN is not a valid number, the user is asked to enter a valid ISBN, and will not continue until a valid ISBN is entered. The code is encapsulated in a try-except block to handle errors. If a ValueError, UnboundLocalError, TypeError or any other error is raised, this prints out flavor text to the user and returns None..

        Args:
            None
        Returns:
            isbn (int): The ISBN the user entered.
            None: If ValueError is raised.
            None: If UnboundLocalError is raised.
            None: If TypeError is raised.
    """
    try:
        isbn = input("Enter the ISBN: ")
        while not isbn.isdigit():
            print("Wrong, only enter numbers, no letters or special characters.")
            isbn = (input("Please enter a valid positive integer for the ISBN: "))
        isbn = int(isbn)
        return isbn
    except ValueError:
        print("Hey now, not cool. Taking you back to the main menu while I clean up the mess you made")
        return None
    except UnboundLocalError:
        print("oh my...  Ok lets get you back to the main menu while I spruse up the place.")
        return None
    except TypeError:
        print("Looks like I dropped the ball on this one.  I will get you back to the main menu while I clean up the mess.")
        return None


def imput_isbn_search()-> int:
    """Summary:
        Asks the user to enter an ISBN. If the ISBN is not a valid number, the user is asked to enter a valid ISBN, and will not continue until a valid ISBN is entered.  The only exception to this is "restart", which will return raise a UnboundLocalError The code is encapsulated in a try-except block to handle errors.  The UnboundLocalError is raised if the user enters "restart" and this returns False. If a TypeError is raised, this returns False.  If a ValueError is raised, this returns False. If a UnboundLocalError is raised, this returns False.  If any other error is raised, this returns False.

        Args:
            None
        Returns:
            isbn (int): The ISBN the user entered.
            False: If ValueError is raised.
            False: If UnboundLocalError is raised.
            False: If TypeError is raised.
            False: If any other error is raised.
    """
    print ("Enter the ISBN of the book you want to search for.  Please watch your capitalization and enter it ver batem.")
    try: 
         isbn = input("Enter the ISBN: ")
         if isbn == "restart":
            raise UnboundLocalError
         if isbn != "restart":
            while not isbn.isdigit():
                print("Wrong, only enter numbers, no letters or special characters.  If you want to restart, enter restart.")
                isbn = (input("Please enter a valid positive integer for the ISBN: "))
            isbn = int(isbn)
            return isbn
    except ValueError:
        return False
    except UnboundLocalError:
        return False
    except TypeError:
        return False
    except Exception as e:
        return False


############################################
def imput_title()-> str:
    """Summery:
        Asks the user to enter a title. Since books can have number, letter and special numbers in them, no real checking is need.  the only issue is to inform the user to watch capitalization and enter it in ver badem, or they will have to go back and delete the book via the main menu.  The code is encapsulated in a try except block to handle errors. If a ValueError, TypeError, or an UnboundLocalError is raised, the function returns  title False as a bool varible. If any other error is raised, the function returns  title False as a bool varible.

        Args:
            None
        
        Returns:
            title (str): The title the user entered.
            False: If ValueError is raised.
            False: If TypeError is raised.
            False: If UnboundLocalError is raised.
            false: If any other error is raised.
    """
    try:
        print ("Please enter the title of the book.  Please watch your capitalization and enter it ver batem.")
        title = input("Please enter the title: ")
        return title
    except ValueError:
        return False
    except TypeError:
        return False
    except UnboundLocalError:
        return False
    except Exception as e:
        return False
##############33
def imput_author()-> str:
    """Summery:
        Asks the user to enter an author. Since authors can have number, letter and special numbers in them, no real checking is need...Authors can be robots or internet users nowadays so its only natural they have odd names.  The only issue is to inform the user to watch capitalization and enter it in ver badem, or they will have to go back and delete the book via the main menu, and returns nothing  The code is encapsulated in a try except block to handle errors.  If there is a ValueError, TypeError, or an UnboundLocalError, the function returns  author False as a bool varible. If any other error is raised, the function returns  author False as a bool varible.

        Args:
            None
        
        Returns:
            author (str): The author the user entered.
            author (bool): If ValueError is raised.
            author (bool): If TypeError is raised.
            author (bool): If UnboundLocalError is raised.
            author (bool): If any other error is raised.
    """
    try:
        print ("Enter the author of the book.  Please watch your capitalization and enter it ver batem.")
        author = input("Please enter the author: ")
        return author
    except ValueError:
        author = False
        author = bool(author)
        author = False
        return author
    except TypeError:
        author = False
        author = bool(author)
        author = False
        return author
    except UnboundLocalError:
        author = False
        author = bool(author)
        author = False
        return author
    except Exception as e:
        author = False
        author = bool(author)
        author = False
        return author
##############333
def imput_name()-> str:
    """Summery:
        Asks the user to enter a name. Since names can have number, letter and special numbers in them, no real checking is need.  the only issue is to inform the user to watch capitalization and enter it in ver badem, or they will have to go back and delete the book via the main menu.  The code is encapsulated in a try except block to handle errors.  If there is a ValueError, the function returns  name False as a bool varible.   If there is a TypeError, the function returns  name False as a bool varible. If any other error is raised, the function returns  name False as a bool varible.

        Args:
            None
        
        Returns:
            name (str): The name the user entered.
            name (bool): If ValueError is raised.
            name (bool): If TypeError is raised.
    """
    try:
        print ("Enter the name of the user.  Please watch your capitalization and enter it ver batem.")
        name = input("Please enter the name: ")
        return name
    except ValueError:
        name = False
        name = bool(name)
        name = False
        return name
    except TypeError:
        name = False
        name = bool(name)
        name = False
        return name
    except Exception as e:
        name = False
        name = bool(name)
        name = False
        return name


#######
def imput_member_id()-> int:
    """Summery:
        Asks the user to enter an ID.  If the ID is not a number, the user is asked to enter a valid ID.  The  The code is encapsulated in a try except block to handle errors.  If there is a ValueError, the function returns  id False as a bool varible.   If there is a TypeError, the function returns  id False as a bool varible. If any other error is raised, the function returns  id False as a bool varible.

        Args:
            None
        
        Returns:
            id (int): The ID the user entered.
            id (bool): If ValueError is raised.
            id (bool): If TypeError is raised.
            id (bool): If any other error is raised.
    """
    try:
        print("Enter the ID of the user. Do not use letters or special characters.")
        id = input("Enter the ID: ")
        while not id.isdigit():
            print("Hold your horses, I said only to enter numbers, that means no letters or special characters.")
            id = input("Please enter a valid  ID number: ")
        id = int(id)
        return id
    except ValueError:
        id  = False
        id = bool(id)
        id = False
        return id
    except TypeError:
        id  = False
        id = bool(id)
        id = False
        return id
    except Exception as e:
        id  = False
        id = bool(id)
        id = False
        return id

the_user = ""
a_user = ""
restore = True
stay = True
def main()-> None:
    """Summery: the main function of the program.  This function is used to call the menu function, and the other functions in the program. if the user chooses to exit, the program ends.  If the user chooses to restart, the program restarts.  If the user chooses to continue, the program continues.  If the user chooses to export the books or users to a csv file, the program exports the books or users to a csv file.  If the user chooses to search for a book or user, the program searches for the book or user.  If the user chooses to check if a book is available, the program checks if the book is available.  If the user chooses to borrow a book, the program borrows the book.  If the user chooses to return a book, the program returns the book.  If the user chooses to add a book, the program adds a book.  If the user chooses to add a user, the program adds a user.  If the user chooses to delete a book, the program deletes a book.  If the user chooses to delete a user, the program deletes a user.  The program has a while loop that keeps the program running until the user chooses to exit.  The code is encapsulated in a try except block to handle errors, except for this main funtion... but if that breaks, the program is useless anyway, but it would never break... probably.

        Args:
            None

        Returns:
            None
    """
    global restore
    global stay
    restore = True
    stay = True
    import csv
    library = Library() #creates a library object
    Walter = True
    while Walter == True: #walter will always be true, bringing it back to choice.  
        print(library)
        choice = menu()
        if choice == "1": #add books
            try:
                print("Add books Selected.  Please answer the following questions to add a book.")
                isbn = imput_isbn()
                if isbn == False:
                    raise TypeError
                title = imput_title()
                if title == False:
                    raise TypeError
                author = imput_author()
                if author == False:
                    raise TypeError
                book = Book(title, author, isbn)
                library.add_book(book) #does this add the book to the library?
                print(library)
                print(f"Book added:  Title: {book.title}, Author: {book.author}, ISBN: {book.isbn},")
            except ValueError:
                print("Error.  Taking you back to the main menu: ")
            except TypeError:
                print("Error.  Taking you back to the main menu: ")
            except UnboundLocalError:
                print("Error.  Taking you back to the main menu: ")
            except AttributeError:
                print("Error.  Taking you back to the main menu: ")
            except NameError:
                print("Error.  Taking you back to the main menu: ")
            except Exception as e:
                print("Error.")
                print(e)
                print("Taking you back to the main menu: ")
        elif choice == "2": #add users
            try:
                print("Add users Selected.  Please answer the following questions to add a user.")
                name = imput_name()
                if name == False:
                    raise TypeError
                id = imput_member_id()
                if id == False:
                    raise TypeError
                user = User(name, id)
                library.add_user(user)
                print(f"User added: {user}")
            except ValueError:
                print("Error.  Taking you back to the main menu: ")
            except TypeError:
                print("Error.  Taking you back to the main menu: ")
            except UnboundLocalError:
                print("Error.  Taking you back to the main menu: ")
            except Exception as e:
                print("Error.")
                print(e)
                print("Taking you back to the main menu: ")
        elif choice == "3": #delete books
            try:
                print("Delete books Selected.")
                print("ok now, I will ask you for the ISBN of the book you want to delete.  If you don't know the ISBN, you can search for the book using the search books option in the menu.")
                billy = True
                billy = continue_question()
                if billy != False:
                    isbn = imput_isbn()
                    book = library.find_book(isbn)
                    if book is not None:
                        library.books.remove(book)
                        print(f"Book deleted: {book}")
                    else:
                        print(f"Book with {isbn} ISBN not found")
                if billy == False:
                    print("Safely landed back at the main menu.")
            except ValueError:
                print("Error.  Taking you back to the main menu: ")
            except TypeError:
                print("Error.  Taking you back to the main menu: ")
            except UnboundLocalError:
                print("Error.  Taking you back to the main menu: ")
            except Exception as e:
                print("Error.")
                print(e)
                print("Taking you back to the main menu: ")
        elif choice == "4": #delete users
            try:
                print("Delete users Selected.")
                print("ok now, I will ask you for the ID of the user you want to delete.  If you don't know the ID, you can search for the user using the search users option in the menu.")
                greg = True
                greg = continue_question()
                if greg != False:
                    id = imput_member_id()
                    global a_user
                    a_user = ""
                    a_user = library.find_user(id)
                    if a_user is not None:
                        library.users.remove(a_user)
                        print(f"User deleted: {a_user}")
                    else:
                        print("User not found")
                if greg == False:
                    print("Safely landed back at the main menu.")
            except ValueError:
                print("Error.  Taking you back to the main menu: ")
            except TypeError:
                print("Error.  Taking you back to the main menu: ")
            except UnboundLocalError:
                print("Error.  Taking you back to the main menu: ")
            except Exception as e:
                print("Error.")
                print(e)
                print("Taking you back to the main menu: ")
        elif choice == "5": #borrow books
            try:
                print("Borrow books Selected.")
                print("ok now, I will ask you for the ISBN of the book you want to borrow.  If you don't know the ISBN, you can search for the book using the search books option in the menu.")
                isbn = imput_isbn_search()
                if isbn != False:
                    book = library.find_book(isbn)
                    if book is not None:
                        print(f"Book found: ")
                        print("Please tell me which user is borrowing the book.  If you don't know the ID, you can search for the user using the search users option in the menu.")
                        id = imput_member_id()
                        user = library.find_user(id)
                        if user is not None: #if the user is found
                            user.borrow_book(book)
                            print(f"Book borrowed: Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
                        else:
                            print("User not found")
                    else:
                        print("Book not found")
                if isbn == False:
                    print("Taking you back to the main menu.")
            except ValueError:
                print("Error.  Taking you back to the main menu: ")
            except TypeError:
                print("Error.  Taking you back to the main menu: ")
            except UnboundLocalError:
                print("Error.  Taking you back to the main menu: ")
            except Exception as e:
                print("Error.")
                print(e)
                print("Taking you back to the main menu: ")
        elif choice == "6": #return books
            try:
                print("Return books Selected.")
                print("ok now, I will ask you for the ISBN of the book you want to return.  If you don't know the ISBN, you can search for the book using the search books option in the menu.")
                isbn = imput_isbn_search()
                if isbn != False:
                    book = library.find_book(isbn)
                    if book is not None:
                        print(f"Book found: {book}")
                        print("Please tell me which user is returning the book.  If you don't know the ID, you can search for the user using the search users option in the menu.")
                        id = imput_member_id()
                        user = library.find_user(id)
                        if user is not None:
                            user.return_book(book)
                            print(f"Book returned: {book}")
                        else:
                            print(f"User {user} not found in the library system")
                    else:
                        print("Book was not found in the library")
                if isbn == False:
                    print("Taking you back to the main menu.")
            except ValueError:
                print("Error.  Taking you back to the main menu: ")
            except TypeError:
                print("Error.  Taking you back to the main menu: ")
            except UnboundLocalError:
                print("Error.  Taking you back to the main menu: ")
            except Exception as e:
                print("Error.")
                print(e)
                print("Taking you back to the main menu: ")
        elif choice == "7":#search books
            try:
                print("Search books Selected.")
                print("ok now, I will ask you for the ISBN of the book you want to search for.  If you don't know the ISBN, you can search for the book using the search books option in the menu.")
                isbn = imput_isbn_search()
                if isbn != False:
                    book = library.find_book(isbn)
                    if book is not None:
                        print(f"Book found:  Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Borrowed: {book.borrowed}")
                    else:
                        print("Book not found")
                if isbn == False:
                    print("Taking you back to the main menu.")
            except ValueError:
                print("Error.  Taking you back to the main menu: ")
            except TypeError:
                print("Error.  Taking you back to the main menu: ")
            except UnboundLocalError:
                print("Error.  Taking you back to the main menu: ")
            except Exception as e:
                print("Error.")
                print(e)
                print("Taking you back to the main menu: ")
        elif choice == "8":#check if book is available to be borrowed
            try:
                print("Check if book is available Selected.")
                print("ok now, I will ask you for the ISBN of the book you want to check.  If you don't know the ISBN, you can search for the book using the search books option in the menu.")
                sassafras = True

                sassafras = continue_question()
                if sassafras != False:
                    isbn = imput_isbn()
                    book = library.find_book(isbn)
                    if book is not None:
                        try:
                            if book.borrowed == True:
                                print(f"Book with isbn:{isbn} is not available")
                            else:
                                print(f"Book with isbn:{isbn} is available")
                        except AttributeError:
                            print("Error.  Taking you back to the main menu: ")
                        except TypeError:
                            print("Error.  Taking you   back to the main menu: ")
                        except Exception as e:
                            print("Error.")
                            print(e)
                            print("Taking you back to the main menu: ")
                    else:
                        print("Book not found")
                if sassafras == False:
                    print("You land roughly and are out for several hours.")
                    print(" You awaken to find yourself back at the main menu fully healed.")
                    print("A wizard must have healed you up while you were out.")
                    print("anyway back to buisness.")
            except ValueError:
                print("Error.  Taking you back to the main menu: ")
            except TypeError:
                print("Error.  Taking you back to the main menu: ")
            except UnboundLocalError:
                print("Error.  Taking you back to the main menu: ")
            except Exception as e:
                print("Error.")
                print(e)
                print("Taking you back to the main menu: ")
        elif choice == "9":#search users
            try:
                print("Search users Selected.")
                print("ok now, I will ask you for the ID of the user you want to search for.  If you don't know the ID, you can search for the user using the search users option in the menu.")
                ID = imput_member_id()
                global the_user
                the_user = ""
                the_user = library.find_user(ID)
                if the_user is not None:
                    print(f"User found: {the_user}")
                else:
                    print(f"User {the_user} not found")
            except ValueError:
                print("Error.  Taking you back to the main menu: ")
            except TypeError:
                print("Error.  Taking you back to the main menu: ")
            except UnboundLocalError:
                print("Error.  Taking you back to the main menu: ")
            except Exception as e:
                print("Error.")
                print(e)
                print("Taking you back to the main menu: ")
        elif choice == "10":#export books to csv
            try:
                print("Export books to csv Selected.")
                print("ok now, I will ask you for the filename you want to export the books to.  If you don't know the filename, you can search for the book using the search books option in the menu.")
                bob  = True
                bob =continue_question()
                if bob != False:
                    print("make sure to add .csv to the end of the filename, or the file will not be saved as a csv file.")
                    filename = input("Enter the filename you want to export the books to: ")
                    library.export_books_to_csv(filename)
                if bob == False:
                    print("After a long journey, you land back at the main menu.  You are tired and need to rest, but there is no time for that.  You must continue.")
                    print("You can't rest with so many people depending on you.")
                    print("You pretend that this converstation did not happen and use the main menu")
            except FileNotFoundError:
                print(" this should not happen... if you see this, please contact the developer.")
                print("Escorting you back to the main menu.")
            except ValueError:
                print("Error.  Taking you back to the main menu: ")
            except TypeError:
                print("Error.  Taking you back to the main menu: ")
            except UnboundLocalError:
                print("Error.  Taking you back to the main menu: ")
            except Exception as e:
                print("Error.")
                print(e)
                print("Taking you back to the main menu: ")
        elif choice == "11":#export users to csv
            try:
                print("Export users to csv Selected.")
                print("ok now, I will ask you for the filename you want to export the users to.  If you don't know the filename, you can search for the user using the search users option in the menu.")
                walrus = True
                walrus = continue_question()
                if walrus != False:
                    print("make sure to add .csv to the end of the filename, or the file will not be saved as a csv file.")
                    filename = input("Enter the filename you want to export the users to: ")
                    library.export_users_to_csv(filename)
                if walrus == False:
                    print("It seems like you are not ready to export users to csv.  You activate the paracute given to you and land back at the main menu.")
            except FileNotFoundError:
                print(" this should not happen... if you see this, please contact the developer.")
                print("Escorting you back to the main menu.")
            except ValueError:
                print("Error.  Taking you back to the main menu: ")
            except TypeError:
                print("Error.  Taking you back to the main menu: ")
            except UnboundLocalError:
                print("Error.  Taking you back to the main menu: ")
            except Exception as e:
                print("Error.")
                print(e)
                print("Taking you back to the main menu: ")
        elif choice == "12":
            try:
                print("Exit Selected.")
                print("Are you sure you want to exit?  All unsaved data will be lost.")
                regret = True
                regret = continue_question()
                if regret != False:
                    print("Goodbye!")
                    quit()
                if regret == False:
                    print("You can't stop, you will not stop. You glide back safely to the main menu with the glider included in your flight.")
                    print("The glider discintegrates after landing and you can no longer use it.")
                    print("You are back at the main menu.")
            except FileNotFoundError:
                print("Wait what? the programm... its malfuntioning!!!  I am taking you back to the main menu.")
            except ValueError:
                print("It seems your computer does not want you to quit.  Spooky...  Taking you back to the main menu: ")
            except TypeError:
                print("Beep boop error...how could this even happen?  Taking you back to the main menu: ")
            except Exception as e:
                print("Error.")
                print(e)
                print("Taking you back to the main menu: ")
        elif choice == "restart":
            try:
                print("Restart Selected.")
                print("congradulations, you have found the secret restart option.  You will be taken back to the main menu.")
            except FileNotFoundError:
                print("Wait what? the programm... its malfuntioning!!!  I am taking you back to the main menu.")
            except ValueError:
                print("It seems your computer does not want you to restart.  Spooky...  Taking you back to the main menu: ")
            except TypeError:
                print("Beep boop error...how could this even happen?  Taking you back to the main menu: ")
            except Exception as e:
                print("Error.")
                print(e)
                print("Taking you back to the main menu: ")

        else:
            try:
                print("Error.  Please use your keyboard to select a valid option from the menu: ")
            except FileNotFoundError:
                print("Wait what? the programm... its malfuntioning!!!  \nThis error should not be possible.  \nI am taking you back to the main menu.")
            except ValueError:
                print("It seems your computer is very comfused.  Have you maintained it properly?\nAnyway...  Taking you back to the main menu: ")
            except TypeError:
                print("Beep boop error...how could this even happen?  Taking you back to the main menu: ")
            except Exception as e:
                print("Error.")
                print(e)
                print("Taking you back to the main menu: ")


    if Walter == False or Walter != True:
        print("Looks like you broke the program.  I hope you are happy with yourself.\nShutting down.")
        quit()

if __name__ == "__main__":
    main()
