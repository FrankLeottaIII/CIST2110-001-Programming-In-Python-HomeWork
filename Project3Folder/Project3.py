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
            Returns a string representation of the book using the following format: ISBN: <ISBN>, Title: <Title>, Author: <Author>, Borrowed: <Borrowed>

            Args:
                None
            
            Returns:
                str: The string representation of the book.
        """
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Borrowed: {self.borrowed}"
#    b. check_out - sets borrowed to True and returns a message that the book has been checked out
    def check_out(self)->str: #says check_out in pytest, fixing it...
        """Summery:
        
        Sets the borrowed attribute to True and returns a message that the book has been checked out.
        
        Args:
            None
            
            Returns:
                str: A message that the book has been checked out."""
        self.borrowed = True
        return f"has been checked out"
#    c. check_in - sets borrowed to False and returns a message that the book has been checked in
    def check_in(self):
        self.borrowed = False
        return f"Book has been checked in"
#    d. borrowed - returns True if the book is borrowed and False if the book is not borrowed
    def borrowed(self)->bool: 
        """Summery:
        This method is used to check to see if a book is borrowed or not.  If it is borrowed, it returns True and if it is not borrowed, it returns False.  The borrowed attribute is set to False by default.
        
        Args:
            None
            
            Returns:
                bool: True if the book is borrowed, False if the book is not borrowed"""
        if self.borrowed == True:
            return True
        else:
            return False


# 2. Create a User class that has the following attributes (create a __init__ method)):
#    a. name (string)
#    c. member_id (int)
#    d. borrowed_books (list of books) - this should not be passed in as a parameter, it should be set to an empty list by default
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES
class User:
    def __init__(self: str, name: int, member_id: int)-> None: #says member_id in pytest instead of ID, fixing it...
        """Summery:
            Initializes a User object with the given attributes: name, and member_id.
            The borrowed_books attribute is set to an empty list by default.

            Args:
                name (str): The name of the user.
                member_id (int): The ID of the user.
            
            Returns:
                None
        """
        self.name: str = name
        self.member_id: int = member_id
        self.borrowed_books: list = [] #says borrowed_books in pytest but barrowed books here, fixing it...

# Methods:
#    a. __str__ (returns a string representation of the user using the following format: Name: <Name>, ID: <ID>, Borrowed Books: <Borrowed Books>)
    def __str__(self)-> str:
        """Summery:
            Returns a string representation of the user using the following format: Name: <Name>, ID: <ID>, Borrowed Books: <Borrowed Books>

            Args:
                None
            
            Returns:
                str: The string representation of the user.
                """
        return f"Name: {self.name}, ID: {self.member_id}, Borrowed Books: {self.borrowed_books}"
#    b. borrow_book - adds the book to the borrowed_books list, updates the borrowed attribute of the book to True, and returns a message that the book has been checked out (should take a book as a parameter)
    def borrow_book(self, book: Book)-> str:
        """Summery:
            Adds the book to the borrowed_books list, updates the borrowed attribute of the book to True, and returns a message that the book has been checked out.

            Args:
                book (Book): The book object to add to the borrowed_books list.

            Returns:
                str: A message that the book has been checked out.
                """
        self.borrowed_books.append(book)
        book.check_out()
        return print("The book has been checked out")
        
#    c. return_book - removes the book from the borrowedBooks list, updates the borrowed attribute of the book to False, and returns a message that the book has been checked in (should take a book as a parameter)
    def return_book(self, book: Book)-> str:
        """Summery:
            Removes the book from the borrowed_books list, updates the borrowed attribute of the book to False, and returns a message that the book has been checked in.

            Args:
                book (Book): The book object to remove from the borrowed_books list.

            Returns:
                str: A message that the book has been checked in.
                """
        self.borrowed_books.remove(book)
        book.check_in()
        return print("The book has been checked in")
# 3. Create a Library class that has the following attributes (create a __init__ method)):
#    a. books (list of books)
#    b. users (list of users)

# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES
class Library:
    def __init__(self)-> None:
        """ Summery:
            Initializes a Library object with the following attributes: books and users.  The books and users attributes are set to empty lists by default.  This is a Library class exclusive method.

            Args:
                None
            
            Returns:
                None
        """
        self.books: list = []
        self.users: list = []
# Methods:
#    a. __str__ (returns a string representation of the library using the following format: Books: <Books>, Users: <Users>)
    def __str__(self)-> str:
        """Summery:
            Returns a string representation of the library using the following format: Books: <Books>, Users: <Users>

            Args:
                None
            
            Returns:
                str: The string representation of the library.
        """
        return f"Books: {self.books}, Users: {self.users}"
#    b. add_book - adds a book to the books list (should take a book as a parameter)
    def add_book(self, book: Book)-> None:
        """Summery:
            Adds a book to the books list.  A book object is passed in as a parameter.  This method does not return anything. This method is exclusive to the Library class.

            Args:
                book (Book): The book object to add to the books list.

            Returns:
                None
            """
        self.books.append(book)

#    c. add_user - adds a user to the users list (should take a user as a parameter)
    def add_user(self, user: User)-> None:
        """Summery:
            Adds a user to the users list.  A user object is passed in as a parameter.  This method does not return anything. This method is exclusive to the Library class.

            Args:
                user (User): The user object to add to the users list.

            Returns:
                None
            """
        self.users.append(user)

#    d. find_book - returns the book with the given ISBN (should take an ISBN as a parameter)
    def find_book(self, isbn: int) -> Book:
        """
            Find a book by its ISBN.   This method takes an ISBN as a parameter. This method searches the book list to see if the paramiter ISBN matches the isbn in the book list.   It returns the book object if found, None otherwise.

        Args:
            isbn (int): The ISBN of the book to find.

        Returns:
            Book: The book object if found, or None otherwise.

        """
        for book in self.books:
            if book.isbn == isbn:
                return book
            return None
  

#    e. find_user - returns the user with the given ID (should take an ID as a parameter)
    def find_user(self, member_id: int) -> User:
        """
        Find a user by their ID.

        Args:
            id (int): The ID of the user to find.

        Returns:
            User: The user object if found, None otherwise.
        """
        for user in self.users:
            if user.member_id == member_id:
                return user
            return None
#    f. export_books_to_csv - exports the books list to a csv file (should take a filename as a parameter)
#       The csv file should have the following format: ISBN,Title,Author,Borrowed
#       The csv.DictWriter class is very useful for this: https://docs.python.org/3/library/csv.html#csv.DictWriter
    def export_books_to_csv(self, filename: str)-> None:
        """
        Export the books list to a csv file. The csv file should have the following format: ISBN,Title,Author,Borrowed.
          If the book is borrowed, the borrowed attribute is exported as True. If the book is not borrowed, the borrowed attribute is 
          exported as False.  If Filename is not found, the user is informed of the error and returned to the main menu.

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
            menu()


#    g. export_users_to_csv - exports the users list to a csv file (should take a filename as a parameter)
#       This will be similar to the export_books_to_csv method but there is a slight difference with the borrowedBooks attribute if you get stuck this code might help:
#       borrowed_books_titles = [book.title for book in user.borrowed_books]
#       Use that and pythons .join method to create a string of the borrowed books titles
    def export_users_to_csv(self, filename)-> None:
        """
        Export the users list to a csv file.  if the user has borrowed books, the borrowed books titles are exported as a string. If the user has not borrowed any books, the borrowed books titles are exported as an empty string. The csv file should have the following format: Name,ID,Borrowed Books.  If Filename is not found, the user is informed of the error and returned to the main menu.

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
            menu()


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
def menu():
    """Summary:
        Lists the menu options for the user to choose from.  The user chooses an option and if the option is valid, the user's choice is returned.    If the option is invalid due to the input not being in the c, the user is asked to choose again, using a while loop.  A list called choice_list  is used to determin if the option is invalid or not.  The choice_list will have all the options in the menu  The user's choice is returned when a valid option is chosen, breaking the while loop.  The code is encapsulated in a try except block to handle errors.

        Args:
            None
        
        Returns:
            choice (str): The user's choice from the menu.
    
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
        choice_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12"]
        while choice not in choice_list:
            choice = input("Error.  Please enter a valid option from the menu: ")
        return choice
    except ValueError:
        choice = input("ValueError.  Please enter a valid option from the menu: ")
        choice_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12"]
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
        If ValueError is raised, the funtion will notify the user of the error and politely return to the menu and returns false.

        Args:
            None
        
        Returns:
            True: If the user enters y or Y.
            False: If the user enters n or N.
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
            menu()
            return False
    except ValueError:
        print("ValueError. Beep boop. escorting you back to the main menu.")
        menu()
        return False
#Methods to use for correct input from user:

def imput_isbn(): 
    """Summary:
        Asks the user to enter an ISBN. If the ISBN is not a valid number, the user is asked to enter a valid ISBN, and will not continue until a valid ISBN is entered. The code is encapsulated in a try-except block to handle errors.

        Args:
            None
        Returns:
            isbn (int): The ISBN the user entered.
            None: If ValueError is raised.
            None: If UnboundLocalError is raised.
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
        menu()
        return None
    except UnboundLocalError:
        print("oh my...  Ok lets get you back to the main menu while I spruse up the place.")
        menu()
        return None



############################################
def imput_title()-> str:
    """Summery:
        Asks the user to enter a title. Since books can have number, letter and special numbers in them, no real checking is need.  the only issue is to inform the user to watch capitalization and enter it in ver badem, or they will have to go back and delete the book via the main menu.  The code is encapsulated in a try except block to handle errors.

        Args:
            None
        
        Returns:
            title (str): The title the user entered.
            None: If ValueError is raised.
    """
    try:
        print ("Please enter the title of the book.  Please watch your capitalization and enter it ver batem.")
        title = input("Please enter the title: ")
        return title
    except ValueError:
        print("Error, the Value is somehow incorrect... anyway let me escort you to the main menu.")
        menu()
        return None
##############33
def imput_author()-> str:
    """Summery:
        Asks the user to enter an author. Since authors can have number, letter and special numbers in them, no real checking is need...Authors can be robots or internet users nowadays so its only natural they have odd names.  The only issue is to inform the user to watch capitalization and enter it in ver badem, or they will have to go back and delete the book via the main menu, and returns nothing  The code is encapsulated in a try except block to handle errors.

        Args:
            None
        
        Returns:
            author (str): The author the user entered.
            None: If ValueError is raised.
    """
    try:
        print ("Enter the author of the book.  Please watch your capitalization and enter it ver batem.")
        author = input("Please enter the author: ")
        return author
    except ValueError:
        print("Error, the Value is somehow incorrect...what a mess. Let me escort you to the main menu while I clean this up for next time.")
        menu()
        return None
##############333
def imput_name()-> str:
    """Summery:
        Asks the user to enter a name. Since names can have number, letter and special numbers in them, no real checking is need.  the only issue is to inform the user to watch capitalization and enter it in ver badem, or they will have to go back and delete the book via the main menu.  The code is encapsulated in a try except block to handle errors.

        Args:
            None
        
        Returns:
            name (str): The name the user entered.
    """
    try:
        print ("Enter the name of the user.  Please watch your capitalization and enter it ver batem.")
        name = input("Please enter the name: ")
        return name
    except ValueError:
        print("Error, the Value is somehow incorrect..which is odd since names are usually cut and dry. Let me escort you to the main menu while I clean this up for next time.")
        menu()
        return None
#######
def imput_member_id()-> int:
    """Summery:
        Asks the user to enter an ID.  If the ID is not a number, the user is asked to enter a valid ID.  The  The code is encapsulated in a try except block to handle errors.

        Args:
            None
        
        Returns:
            id (int): The ID the user entered.
            None: If ValueError is raised.
    """
    try:
        print("Enter the ID of the user. Do not use letters or special characters.")
        id = input("Enter the ID: ")
        while id not in id.isdigit():
            print("Hold your horses, I said only to enter numbers, that means no letters or special characters.")
            id = input("Please enter a valid  ID number: ")
        id = int(id)
        return id
    except ValueError:
        print("Error Error Error beep boop.  I am malfuntioning so you are being ushered into the  main menu.")
        menu()
        return None
    except TypeError:
        print("Error Error Error beep boop.  I am malfuntioning so you are being ushered into the  main menu.")
        menu()
        return None

def main():
    import csv
    library = Library()
    menu()
    Walter = True
    while Walter == True:
        if choice == "1": #add books
            print("Add books Selected.  Please answer the following questions to add a book.")
            isbn = imput_isbn()
            title = imput_title()
            author = imput_author()
            book = Book(title, author, isbn)
            library.add_book(book)
            print(f"Book added: {book}")
            menu()
        elif choice == "2": #add users
            print("Add users Selected.  Please answer the following questions to add a user.")
            name = imput_name()
            id = imput_member_id()
            user = User(name, id)
            library.add_user(user)
            print(f"User added: {user}")
            menu()
        elif choice == "3": #delete books
            print("Delete books Selected.")
            print("ok now, I will ask you for the ISBN of the book you want to delete.  If you don't know the ISBN, you can search for the book using the search books option in the menu.")
            continue_question()
            isbn = imput_isbn()
            book = library.find_book(isbn)
            if book is not None:
                library.books.remove(book)
                print(f"Book deleted: {book}")
            else:
                print(f"Book with {isbn} ISBN not found")
                menu()
        elif choice == "4": #delete users
            print("Delete users Selected.")
            print("ok now, I will ask you for the ID of the user you want to delete.  If you don't know the ID, you can search for the user using the search users option in the menu.")
            continue_question()
            id = imput_member_id()
            user = library.find_user(id)
            if user is not None:
                library.users.remove(user)
                print(f"User deleted: {user}")
            else:
                print("User not found")
                menu()
        elif choice == "5": #borrow books
            print("Borrow books Selected.")
            print("ok now, I will ask you for the ISBN of the book you want to borrow.  If you don't know the ISBN, you can search for the book using the search books option in the menu.")
            continue_question()
            isbn = imput_isbn()
            book = library.find_book(isbn)
            if book is not None:
                print(f"Book found: {book}")
                print("Please tell me which user is borrowing the book.  If you don't know the ID, you can search for the user using the search users option in the menu.")
                continue_question()
                id = imput_member_id()
                user = library.find_user(id)
                if user is not None:
                    user.borrow_book(book)
                    print(f"Book borrowed: {book}")
                else:
                    print("User not found")
                    menu()
            else:
                print("Book not found")
                menu()
            menu()
        elif choice == "6": #return books
            print("Return books Selected.")
            print("ok now, I will ask you for the ISBN of the book you want to return.  If you don't know the ISBN, you can search for the book using the search books option in the menu.")
            continue_question()
            isbn = imput_isbn()
            book = library.find_book(isbn)
            if book is not None:
                print(f"Book found: {book}")
                print("Please tell me which user is returning the book.  If you don't know the ID, you can search for the user using the search users option in the menu.")
                continue_question()
                id = imput_member_id()
                user = library.find_user(id)
                if user is not None:
                    user.return_book(book)
                    print(f"Book returned: {book}")
                else:
                    print(f"User {user} not found in the library system")
            else:
                print("Book was not found in the library")
            menu()
        elif choice == "7":#search books
            print("Search books Selected.")
            print("ok now, I will ask you for the ISBN of the book you want to search for.  If you don't know the ISBN, you can search for the book using the search books option in the menu.")
            continue_question()
            isbn = imput_isbn()
            book = library.find_book(isbn)
            if book is not None:
                print(f"Book found: {book}")
            else:
                print("Book not found")
                menu()
        elif choice == "8":#check if book is available to be borrowed
            print("Check if book is available Selected.")
            print("ok now, I will ask you for the ISBN of the book you want to check.  If you don't know the ISBN, you can search for the book using the search books option in the menu.")
            continue_question()
            isbn = imput_isbn()
            book = library.find_book(isbn)
            if book is not None:
                if book.borrowed():
                    print(f"Book with isbn: {isbn} is not available")
                else:
                    print(f"Book with isbn: {isbn} is available")
            else:
                print("Book not found")
            menu()
        elif choice == "9":#search users
            print("ok now, I will ask you for the ID of the user you want to search for.  If you don't know the ID, you can search for the user using the search users option in the menu.")
            id = input("Enter the ID of the user you want to search for: ")
            user = library.find_user(id)
            if user is not None:
                print(f"User found: {user}")
            else:
                print(f"User {user} not found")
            menu()
        elif choice == "10":#export books to csv
            print("Export books to csv Selected.")
            print("ok now, I will ask you for the filename you want to export the books to.  If you don't know the filename, you can search for the book using the search books option in the menu.")
            continue_question()
            print("make sure to add .csv to the end of the filename, or the file will not be saved as a csv file.")
            filename = input("Enter the filename you want to export the books to: ")
            library.export_books_to_csv(filename)
            menu()
        elif choice == "11":#export users to csv
            print("Export users to csv Selected.")
            print("ok now, I will ask you for the filename you want to export the users to.  If you don't know the filename, you can search for the user using the search users option in the menu.")
            continue_question()
            print("make sure to add .csv to the end of the filename, or the file will not be saved as a csv file.")
            filename = input("Enter the filename you want to export the users to: ")
            library.export_users_to_csv(filename)
            menu()
        elif choice == "12":
            print("Goodbye!")
            quit()
        else:
            print("Error.  Please enter a valid option from the menu: ")
            menu()
    Walter = True
Walter = True


if __name__ == "__main__":
    main()
