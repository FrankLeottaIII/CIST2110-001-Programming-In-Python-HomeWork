#  ________  ________  ________        ___  _______   ________ _________        ________
# |\   __  \|\   __  \|\   __  \      |\  \|\  ___ \ |\   ____\\___   ___\     |\_____  \
# \ \  \|\  \ \  \|\  \ \  \|\  \     \ \  \ \   __/|\ \  \___\|___ \  \_|     \|____|\ /_
#  \ \   ____\ \   _  _\ \  \\\  \  __ \ \  \ \  \_|/_\ \  \       \ \  \            \|\  \
#   \ \  \___|\ \  \\  \\ \  \\\  \|\  \\_\  \ \  \_|\ \ \  \____   \ \  \          __\_\  \
#    \ \__\    \ \__\\ _\\ \_______\ \________\ \_______\ \_______\  \ \__\        |\_______\
#     \|__|     \|__|\|__|\|_______|\|________|\|_______|\|_______|   \|__|        \|_______|
# Author:
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
#    a. ISBN (int)
#    b. Title (string)
#    c. Author (string)
#    d. borrowed (boolean) - this should not be passed in as a parameter, it should be set to False by default
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES
class Book:
    def __init__(self, isbn, title, author):
        self.isbn: int = isbn
        self.title: str = title
        self.author: str = author
        self.borrowed: bool = False
# Methods:
#    a. __str__ (returns a string representation of the book using the following format: ISBN: <ISBN>, Title: <Title>, Author: <Author>, Borrowed: <Borrowed>)
#    b. checkout - sets borrowed to True and returns a message that the book has been checked out
#    c. checkin - sets borrowed to False and returns a message that the book has been checked in
#    d. isBorrowed - returns True if the book is borrowed and False if the book is not borrowed
    def __str__(self):
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Borrowed: {self.borrowed}"

    def checkout(self):
        self.borrowed = True
        return f"Book has been checked out"
    
    def checkin(self):
        self.borrowed = False
        return f"Book has been checked in"
    
    def isBorrowed(self):
        if self.borrowed == True:
            return True
        else:
            return False
# 2. Create a User class that has the following attributes (create a __init__ method)):
#    a. Name (string)
#    c. ID (int)
#   d. borrowedBooks (list of books)
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES
class User:
    def __init__(self, name, id):
        self.name: str = name
        self.id: int = id
        self.borrowed_books: list = []
    

    

# Methods:
#    a. __str__ (returns a string representation of the user using the following format: Name: <Name>, ID: <ID>, Borrowed Books: <Borrowed Books>)
    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, Borrowed Books: {self.borrowed_books}"
#    b. borrow_book - adds the book to the borrowedBooks list, updates the isBorrowed attribute of the book to True, and returns a message that the book has been checked out (should take a book as a parameter)
    def borrow_book(self, book: Book):
        self.borrowed_books.append(book)
        book.checkout()
        return f"Book has been checked out"
#    c. return_book - removes the book from the borrowedBooks list, updates the isBorrowed attribute of the book to False, and returns a message that the book has been checked in (should take a book as a parameter)
    def return_book(self, book: Book):
        self.borrowed_books.remove(book)
        book.checkin()
        return f"Book has been checked in"
# 3. Create a Library class that has the following attributes (create a __init__ method)):
#    a. books (list of books)
#    b. users (list of users)
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES
class Library:
    def __init__(self):
        self.books: list = []
        self.users: list = []
# Methods:
#    a. __str__ (returns a string representation of the library using the following format: Books: <Books>, Users: <Users>)
    def __str__(self):
        return f"Books: {self.books}, Users: {self.users}"
#    b. add_book - adds a book to the books list (should take a book as a parameter)
    def add_book(self, book: Book):
        self.books.append(book)
#    c. add_user - adds a user to the users list (should take a user as a parameter)
    def add_user(self, user: User):
        self.users.append(user)
#    d. find_book - returns the book with the given ISBN (should take an ISBN as a parameter)
    def find_book(self, isbn: str) -> Book:
        """
            Find a book by its ISBN.

        Args:
            isbn (str): The ISBN of the book to find.

        Returns:
            Book: The book object if found, None otherwise.
        """
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
#    e. find_user - returns the user with the given ID (should take an ID as a parameter)
    def find_user(self, id: int) -> User:
        """
        Find a user by their ID.

        Args:
            id (int): The ID of the user to find.

        Returns:
            User: The user object if found, None otherwise.
        """
        for user in self.users:
            if user.id == id:
                return user
        return None
#    f. export_books_to_csv - exports the books list to a csv file (should take a filename as a parameter)
#       The csv file should have the following format: ISBN,Title,Author,Borrowed
#       The csv.DictWriter class is very useful for this: https://docs.python.org/3/library/csv.html#csv.DictWriter
    def export_books_to_csv(self, filename):
        """
        Export the books list to a csv file.

        Args:
            filename (str): The name of the file to export to.
        """
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["ISBN", "Title", "Author", "Borrowed"])
            writer.writeheader()
            for book in self.books:
                writer.writerow({"ISBN": book.isbn, "Title": book.title, "Author": book.author, "Borrowed": book.borrowed})


#    g. export_users_to_csv - exports the users list to a csv file (should take a filename as a parameter)
#       This will be similar to the export_books_to_csv method but there is a slight difference with the borrowedBooks attribute if you get stuck this code might help:
#       borrowed_books_titles = [book.title for book in user.borrowed_books]
#       Use that and pythons .join method to create a string of the borrowed books titles
    def export_users_to_csv(self, filename):
        """
        Export the users list to a csv file.

        Args:
            filename (str): The name of the file to export to.
        """
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "ID", "Borrowed Books"])
            for user in self.users:
                borrowed_books_titles = [book.title for book in user.borrowed_books]
                writer.writerow([user.name, user.id, ", ".join(borrowed_books_titles)])
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

#Methods to 


def main():
    import csv
    library = Library()
    menu()
    Walter = True
    while Walter == True
        if choice == "1": #add books
            isbn = input("Enter the ISBN: ")
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            book = Book(isbn, title, author)
            library.add_book(book)
            print(f"Book added: {book}")
            menu()
        elif choice == "2": #add users
            name = input("Enter the name: ")
            id = input("Enter the ID: ")
            user = User(name, id)
            library.add_user(user)
            print(f"User added: {user}")
            menu()
        elif choice == "3": #delete books
            isbn = input("Enter the ISBN of the book you want to delete: ")
            book = library.find_book(isbn)
            if book is not None:
                library.books.remove(book)
                print(f"Book deleted: {book}")
            else:
                print(f"Book not found")
            menu()
        elif choice == "4": #delete users
            id = input("Enter the ID of the user you want to delete: ")
            user = library.find_user(id)
            if user is not None:
                library.users.remove(user)
                print(f"User deleted: {user}")
            else:
                print(f"User not found")
            menu()
        elif choice == "5": #borrow books
            isbn = input("Enter the ISBN of the book you want to borrow: ")
            book = library.find_book(isbn)
            if book is not None:
                id = input("Enter the ID of the user that is borrowing the book: ")
                user = library.find_user(id)
                if user is not None:
                    user.borrow_book(book)
                    print(f"Book borrowed: {book}")
                else:
                    print(f"User not found")
            else:
                print(f"Book not found")
            menu()
        elif choice == "6": #return books
            isbn = input("Enter the ISBN of the book you want to return: ")
            book = library.find_book(isbn)
            if book is not None:
                id = input("Enter the ID of the user that is returning the book: ")
                user = library.find_user(id)
                if user is not None:
                    user.return_book(book)
                    print(f"Book returned: {book}")
                else:
                    print(f"User not found")
            else:
                print(f"Book not found")
            menu()
        elif choice == "7":#search books
            isbn = input("Enter the ISBN of the book you want to search for: ")
            book = library.find_book(isbn)
            if book is not None:
                print(f"Book found: {book}")
            else:
                print(f"Book not found")
            menu()
        elif choice == "8":#check if book is available to be borrowed
            isbn = input("Enter the ISBN of the book you want to check: ")
            book = library.find_book(isbn)
            if book is not None:
                if book.isBorrowed():
                    print(f"Book is not available")
                else:
                    print(f"Book is available")
            else:
                print(f"Book not found")
            menu()
        elif choice == "9":#search users
            id = input("Enter the ID of the user you want to search for: ")
            user = library.find_user(id)
            if user is not None:
                print(f"User found: {user}")
            else:
                print(f"User not found")
            menu()
        elif choice == "10":#export books to csv
            filename = input("Enter the filename you want to export the books to: ")
            library.export_books_to_csv(filename)
            menu()
        elif choice == "11":#export users to csv
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



if __name__ == "__main__":
    main()
