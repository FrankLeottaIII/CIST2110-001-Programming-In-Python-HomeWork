# Project 2
# Name:
"""NEED TO
later fix the add contact funtions, notable the get stuff.
try and except needed for each get function notably

"""
# Project 2 will test on topics learned in class so far. You will be creating a contact list program with an external csv file that will store the contacts. The program will have the following features:
# 1. Add contact
# 2. View contacts
# 3. Delete contact
# 4. Save contacts to csv file
# 5. Next Birthday
# 0. Quit
#
# Import the csv module, datetime module
import csv
import datetime as dt
import time

# Make sure to show docs strings for each function and include comments in your code. Make sure to include a main function and call the main function at the end of the program.

# print("Welcome to the Contact List Program")

# There is also a contact.csv file that will be used to store the contacts. The csv file will have the following format:
# Name,Phone,Email,Birthday
# The program will be menu driven and will display the menu as shown above. The program will run until the user selects option 0 to quit. The program will be implemented in a file called Project2.py. The program will use the following functions:


# import_csv - This function will import the contacts from the csv file. The function will return a dictionary of contacts. The key will be the name of the contact and the value will be a dictionary containing the phone number, email address, and birthday. The function will take one parameter, the name of the csv file. The function will display an error message if the file does not exist. The function will display a message if the file exists and the contacts were imported successfully.
# Hint1: Use the csv module to read the csv file. Use the csv.reader function. IE. reader = csv.reader(file)
# Hint2: You will need to skip the first line of the csv file since it contains the column headers. You can do that with the next function. IE. next(reader)
# Hint3: You will need to create a dictionary of contacts. You can do that by looping through the reader object. IE. for row in reader:
# Hint4: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(row[3], '%m/%d/%Y')
# Hint5: You will need to create a dictionary of the phone number, email address, and birthday. You can do that by creating a dictionary and adding the values to the dictionary. IE. contact[row[0]] = {'Phone': row[1], 'Email': row[2], 'Birthday': dt.datetime.strptime(row[3], '%m/%d/%Y')}
# Hint6: Use the FileNotFoundError exception to catch if the file does not exist.
contacts = {}

def import_csv(csv_file):
    """Summery:
    Import the contacts from the csv file.
    
    Args:   
        csv_file (str): The name of the csv file to import.
        
    Returns:
        dict: A dictionary of contacts, with each contact having a dictionary associeated with them,
            The contact name is the key, the contact info dictionary contents is the value. 
            The contact info dictionary has the following keys: 'Name', 'Phone', 'Email', 'Birthday'
                       """
    try:
        with open(csv_file, 'r') as file: # open file in read mode
            reader = csv.reader(file) # create reader object, a reader object is an iterator.  It will read one line at a time
            next(reader)  # Skip the first line
            global contacts
            contacts = {} # create empty dictionary
            for row in reader: # loop through reader object, to define the values of the dictionary
                name = row[0] # name is the key, row[0] is the first column in the csv file
                phone = row[1] # phone is the key, row[1] is the second column in the csv file
                email = row[2]
                birthday = dt.datetime.strptime(row[3], '%m/%d/%Y')
                name2 = name
                #birthday = dt.datetime.strptime(row[3], '%m/%d/%Y') # 
                contacts[name2] = {'Name': name,'Phone': phone, 'Email': email, 'Birthday': birthday} 
            print("Contacts imported successfully.")
            return contacts
    except FileNotFoundError:
        print("File does not exist.")
    except IndexError:
        print("IndexError: list index out of range")

contacts = import_csv("contacts.csv")    

# -------------------------------------------------------------------------------------

# add_contact(name, phone, email, birthday) - This function will add a contact to the dictionary. 
# The function will take four parameters, the name, phone number, email address, and birthday.
#  The function will return True if the contact was added and False if the contact was not added. 
# The function will display an error message if the contact already exists.
# Hint 1: You will need to convert the birthday to a datetime object.
#  You can do that by using the strptime function. IE. dt.datetime.strptime(birthday, '%m/%d/%Y')
# Hint 2: To add a contact to the dictionary, you need to use the key as the name and the values as a 
# dictionary that contains the phone number, email address, and birthday. To reference the specific key you can use contact[name]

# global variables for add_contact() stuff:
NAME = ""
PHONE = ""
EMAIL = ""
BIRTHDAY = ""
WALDO = ""

#------------------------Functions for add_contact() stuff------------------------
def get_name()-> str:
    """ Summery:
    Get the name from the user.
    Uses the global varible NAME

    Loops if: both the lasts name and the first name are not in the correct format with a while loop.. loops seperately.

    Args:
        None

    Returns:
        str: The name for this person in the NAME varible.
    """
    global NAME
    try:  
        first_name = input("Enter the first name. It is case sensitive: ")
        while not first_name.isalpha(): # if the name is not all letters
            print("Hey now, No numbers or special characters allowed in the name, please try again Parnter")
            print("That includes spaces and grammer... remember, this is a name, not a sentence")
            first_name = input("Enter name, This is case sensitive : ")
        first_name = first_name.title() # makes the first letter of the first name capitalized
        last_name = input("Enter the last name. It is case sensitive: ")
        while not last_name.isalpha(): # if the name is not all letters
            print("Hey now, No numbers or special characters allowed in the name, please try again Bucko")
            print("That includes spaces and grammer... remember, this is a name, not a sentence")
            last_name = input("Enter name, This is case sensitive : ")
        last_name = last_name.title() # makes the first letter of the last name capitalized
        NAME = f"{first_name} {last_name}"
        return NAME
    except ValueError:
        print("Error: cannot add contact due to ValueError")


FIRST_THREE = ""
SECOND_THREE = ""
LAST_FOUR = ""

def first_three_fun()-> str:
    """ Summery:
    Get the first three digits of the phone number from the user.
    Uses the global varible FIRST_THREE

    Loops if: the phone number is not in the correct format with a while loop.

    Agrs:
        None

    Returns:
        str: The first three digits of the phone number.
    """
    global FIRST_THREE
    print(" I will need the phone number in the following format: 123-456-7890")
    try:
        FIRST_THREE = input("Enter the first three digits of the phone number: ")
        while not FIRST_THREE.isdigit() or len(FIRST_THREE) != 3:
            print("Invalid input, please try again")
            FIRST_THREE = input("Enter the first three digits of the phone number: ")
        return FIRST_THREE
    except ValueError:
        print("Error: lets try that again")

def second_three_fun() -> str:
    """Summery:
    Get the second three digits of the phone number from the user.

    Args:
        None

    Returns:
        str: The second three digits of the phone number.
    """
    global SECOND_THREE
    try:
        SECOND_THREE = input("Enter the second three digits of the phone number: ")
        while not SECOND_THREE.isdigit() or len(SECOND_THREE) != 3:
            print("Invalid input, lets try that again")
            SECOND_THREE = input("Enter the second three digits of the phone number: ")
        return SECOND_THREE
    except ValueError:
        print("Error: lets try that again")


def last_four_fun()-> str:
    """Summery:
    Get the last four digits of the phone number from the user.

    Args:
        None

    Returns:
        str: The last four digits of the phone number.

    """
    global LAST_FOUR
    try:
        LAST_FOUR = input("Enter the last four digits of the phone number: ")
        while not LAST_FOUR.isdigit() or len(LAST_FOUR) != 4:
            print("Invalid input, lets try that again")
            LAST_FOUR = input("Enter the last four digits of the phone number: ")
        return LAST_FOUR
    except ValueError:
        print("Error: lets try that again")

def get_phone() -> str:
    """Summery:
    Combines the FIRST_THREE, SECOND_THREE, and LAST_FOUR variables of the phone number into one string.
    Global variables used: FIRST_THREE, SECOND_THREE, LAST_FOUR, PHONE
    Functions used in this function: first_three_fun(), second_three_fun(), last_four_fun()

    Loops if the phone number is not in the correct format.

    Args:
        None
    
    Returns:
        str: The phone number in the format xxx-xxx-xxxx in the PHONE variable.
    """
    try:
        global PHONE
        global FIRST_THREE
        global SECOND_THREE
        global LAST_FOUR
        first_three_fun()
        second_three_fun()
        last_four_fun()
        PHONE = f"{FIRST_THREE}-{SECOND_THREE}-{LAST_FOUR}"
        return PHONE
    except ValueError:
        print("ValueError: let's try that again...")


def get_email()-> str:
    """Summery:
    Get the email from the user.
    Uses the global varible EMAIL

    loops if: the email is not in the correct format.  May cause colorblindness.

    Args:
        None

    returns:
        str: The email for this person in the EMAIL varible.

    regrets:
        None
        """
    global EMAIL
    try:
        EMAIL = input("Enter email: ")
        EMAIL = EMAIL.strip()
        red = True
        green = False
        while red == True:
            if "@" not in EMAIL or "." not in EMAIL:
                print("Invalid email, all emails have a @ and a period Please try again")
                EMAIL = input("Enter email: ")
                red = True
            elif "@" in EMAIL and "." in EMAIL:
                red = False
                green = True    # You are colorblind now from this point on, sorry
        return EMAIL
    except ValueError:
        print("Error: cannot add contact due to ValueError")




def get_birthday()-> dt.datetime:
    """Summery:
    Get the birthday from the user, and turns it into a datetime object string via .strptime(Birthday,'%m/%d/%Y').
    Uses the global varible BIRTHDAY

    loops if: the birthday is not in the correct format.

    Args:
        None
    
    Returns:
        dt.datetime: The birthday for this person in the BIRTHDAY varible.
    
    Sanity level after writing this funtion:
        100% sane, no problems here, no sir...probably. Datetime objects are aggrivating.

    """
    global BIRTHDAY
    while True:
        try:
            BIRTHDAY = input("Enter birthday in this format: (mm/dd/yyyy): ")
            dt.datetime.strptime(BIRTHDAY, '%m/%d/%Y')
            break
        except ValueError:
            print("Invalid date format. Please enter the birthday in the format mm/dd/yyyy.")
    BIRTHDAY = dt.datetime.strptime(BIRTHDAY, '%m/%d/%Y')
    return BIRTHDAY





def get_contact_info()-> dict:
    """Summery:
    Get the contact info from the user, and puts it into the contacts dictionary.
    Uses the global varibles NAME, PHONE, EMAIL, BIRTHDAY, contacts

    Used funtions in this funtion: get_name(), get_phone(), get_email(), get_birthday()

    Args:
        None

    Returns:
        dict: The contact info for this person in the contacts dictionary.
    """
    global NAME
    global PHONE
    global EMAIL
    global BIRTHDAY
    try:
        print("Ok, now lets get the contact info for this person")
        print("lets start with the name, I'll ask for the first and last name seperatly")
        get_name()
        get_phone()
        get_email()
        get_birthday()
        contacts[NAME] = {'Name': NAME, 'Phone': PHONE, 'Email': EMAIL, 'Birthday': BIRTHDAY}
        return contacts[NAME]
    except ValueError:
        print("Error: cannot add contact to dictionary due to ValueError")


def add_contact(name, phone, email, birthday) -> bool:
    """Summery:
        Checks to see if the contact is already in the contacts dictionary, if not, adds the contact to the contacts dictionary.
        Uses the global varibles NAME, PHONE, EMAIL, BIRTHDAY, contacts
    
        Args:   
            name (str): The name of the contact.
            phone (str): The phone number of the contact.
            email (str): The email of the contact.
            birthday (str): The birthday of the contact.
        Note: the only reason I put them here is due to the assighnment saying to do so, they aren't doing anything since I already put them in the contacts dictionary in the get_contact_info() funtion.
            I guess they are on vacation, or something... I don't know, I'm not their boss.
            i think... is someone truly a boss of a varible? I mean, they are just a bunch of 1's and 0's, right?
            anyway...
          
        
        Returns:
            bool: True if the contact was successfully added and/or updated, False otherwise.

    """
    name
    phone
    email
    birthday
    try:
        global contacts
        if name in contacts.keys(): # if the name is in the keys
            print("Contact Sucessfully added and/or updated")
            return True
        elif name not in contacts:
            contacts[name] = {'Name': name, 'Phone': phone, 'Email': email, 'Birthday': birthday}
            print("Contact sucessfully added")
            return True
        else:
            print("Error: contact not added")
            return False
    except ValueError:
        print("Error: cannot add contact due to ValueError")
        return False

#-------------------------------------------------------------------------------------

#2.) view_contacts() - This function will display the contacts in the dictionary. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. Use string formatting to display the contacts in a table format. The table should have a header row and each contact should be on a separate row. The table should have the following columns: Name, Phone, Email, Birthday. The birthday should be formatted as mm/dd/yyyy. The table should be sorted by name.

def view_contacts()-> None: # none is the same as void in java, it means that the function returns nothing, it is a place holder.
    """
    Display the contacts in the dictionary in a table format.
    For each contact in contacts, print the contact info in a table format.
    If there are no contacts in the dictionary, prints a message saying so.

    Args:
        None 
    
    Returns:
        None
    """
    global contacts
    try:
        if len(contacts) == 0:
            print("There are no contacts in the dictionary.")
        else:
            print("Name\tPhone\tEmail\tBirthday")
            for name, contact in contacts.items():
                print(f'{name}\t{contact["Phone"]}\t{contact["Email"]}\t{contact["Birthday"]}')
    except ValueError:
        print("Error: cannot view contacts due to ValueError")


# Hint 1: You will need to loop through the dictionary to display the contacts. IE. for key, value in contact.items():
# Extra Credit: The data is a dictionary of dictionaries. You can unpack the dictionary into a list of dictionaries.
#  Like in Lab 10 and then use the tabulate library to display the contacts in a table format.
#  This is optional and not required. You can use string formatting to display the contacts in a table format.
#from IPython.display import display

# import pandas as pd
def panda_display()-> None:
    """Summery:
    desplays the contacts in a table format using the pandas module.

    args:
        None
    
    Moduals used:
        pandas
    
    Returns:
        Prints the contacts in a table format, using the pandas module.
        or
        None if ValueError or ModuleNotFoundError
    
    """
    global contacts
    try:
        df = pd.DataFrame(contacts.values(), columns=['Name', 'Phone', 'Email', 'Birthday'])
        print(df)
    except ValueError:
        print("Error: cannot view contacts due to ValueError")
        return None
    except ModuleNotFoundError:
        print("Error: No module named 'pandas', cannot view contacts due to ModuleNotFoundError")
        return None
    except NameError: #its supposed to fail the first time to install pandas, so it can be imported.  it will work correctly the next time
        import pandas as pd
        df = pd.DataFrame(contacts.values(), columns=['Name', 'Phone', 'Email', 'Birthday'])
        print(df)
    df = pd.DataFrame(contacts.values(), columns=['Name', 'Phone', 'Email', 'Birthday'])
#     print(df)
# print(df)
# print("\n\n\n")
# print(df)
# def unpack_dict(dictionary, list_varible):
#     """
#     Unpacks a dictionary into a list of dictionaries.

#     Args:
#         dictionary (dict): The dictionary to be unpacked.

#     Returns:
#         list: A list of dictionaries containing the unpacked data.
#     """
#     try:
#         list_varible = []
#         for key, value in dictionary.items():
#             list_varible.append({key: value})
#         return list_varible
#     except ValueError:
#         print("Error: cannot unpack dictionary due to ValueError")
#     except TypeError:
#         print("Error: cannot unpack dictionary due to TypeError")
# list_of_dicts = []
# unpack_dict(contacts, list_of_dicts)

# # not right , need 
# from IPython.display import display
# import pandas as pd

# def panda_dict(list_varible):
#     """Summery:
#     Displays the contacts in the dictionary in a table format."""
#     try:
#         list_varible = pd.DataFrame(dict)
#         list_varible = display(list_varible)
#         return list_varible
#     except ValueError:
#         print("Error: cannot unpack dictionary due to ValueError")
#         return None
#     except ModuleNotFoundError:
#         print("Error: No module named 'pandas', cannot unpack dictionary due to ModuleNotFoundError")
#         return None
# # unpack_dict2(contacts)
# # list_of_dict = pd.DataFrame(dict)
# # display(list_of_dict)
# print(panda_dict(contacts))

#will run it to see the errors, and ajust accordingly




#____----------------------------

# delete_contact(id) - This function will delete a contact from the dictionary. 
# The function will take one parameter, the name of the contact to delete.
#  The function will return True if the contact was deleted and False if the contact was not deleted.
#  The function will display an error message if the contact does not exist.


def delete_contact(do_I_delete_contact: bool) -> bool:
    """
    part one of a process of deleting a contact from the contacts dictionary.

    Args:
        do_I_delete_contact (bool): A boolean value indicating whether to delete the contact or not.

    Returns:
        bool: True if the contact is successfully deleted, False otherwise.
    """
    global contacts
    global NAME
    if NAME in keys:
        # del contacts[name]
        return True
    else:
        print("Error: Contact does not exist")
        return False

def delete_contact_action(question):
    """
    part two of a process of deleting a contact from the contacts dictionary.
    
    Args:
        question (bool): A boolean value indicating whether to delete the contact or not.
        
        Returns:
            None 
        """
    try:
        if question == True:
            del contacts[NAME]
            print("Contact deleted")
        elif question == False:
            print("Contact not deleted")
        else:
            print("Error: Contact does not exist")
    except ValueError:
        print("Error: Contact does not exist")



#-------------------------------------------------------------------------------------
def next_birthday():
    """
    Display the next birthday in the contacts dictionary.

    For each contact in contacts, check the birthday value of that contact.
    If the birthday is in the next 30 days, print the next birthday and the directory name.
    If there are no birthdays in the next 30 days, print a message saying so.
    If there are no contacts in the dictionary, print a message saying so.

    Returns:
        None
    """
    today = dt.date.today()
    next_birthday_date = None
    next_birthday_name = None

    for contact_name, contact_info in contacts.items():
        contact_birthday = contact_info.get('Birthday')
        contact_birthday = dt.datetime.now().date()
        contact_birthday = contact_birthday.strftime('%Y-%m-%d %H:%M:%S')
        contact_birthday = dt.datetime.strptime(contact_birthday, '%Y-%m-%d %H:%M:%S').date()
        #if contact_birthday:
            # convert the datetime object to a string
            #contact_birthday = dt.datetime.strptime(contact_birthday, "%m/%d/%Y").date()
        if (contact_birthday - today).days <= 30:
            if next_birthday_date is None or contact_birthday < next_birthday_date:
                next_birthday_date = contact_birthday
                next_birthday_name = contact_name

    if next_birthday_date is not None and len(contacts) > 0:
        birthday_message = f"The next birthday belongs to {next_birthday_name}, on this date: {next_birthday_date.strftime('%m/%d/%Y')}"
        print(birthday_message)
    elif len(contacts) == 0:
        print("There are no contacts in the dictionary.")
        imput = "restart"
    else:
        print("error")

#
#-------------------------------------------------------------------------------------
# save_csv(filename) - This function will save the contacts to the csv file. Prompt the user to enter a filename to save the contacts to. If the file exists, overwrite the file. If the file does not exist, create the file. The function will return True if the contacts were saved and False if the contacts were not saved.
import csv
question = ""
the_filename = ""
def save_csv()-> str:
    """Summery:
    Asks the user if they want to save the contacts to a csv file, but doesn't save them, just asks to see if they want to.
    relys on the save_
    
    
    """
    global imput
    global the_filename
    question = input("Would you like to save the contacts to a csv file? (y/n): ")
    if question.lower() == 'y':
        the_filename = input("Enter the filename to save the contacts to: ")
        return the_filename
    else:
        print(".....")
        imput = "restart"
        return imput #this approch doesnt work, but its funnier to let it go to fileNotFound error in the save_csv_action() funtion.

def save_csv_action(filename):
    """Summery:
    This funtion Saves the contacts to the csv file.
    Uses the global varible contacts
    This function is the action part of the save_csv() funtion.
    This funtion only returns False if the file is not found, otherwise it runs normally.


    Args:
        filename (str): The name of the csv file to save the contacts to.
    
    Returns:
        bool: True if the contacts were saved, False otherwise.
    """
    global greg
    try:
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone', 'Email', 'Birthday'])
            for contact in contacts.values(): # Loop through the contacts dictionary, the values are the inner dictionaries(how you deal with inner dictionaries)
                contact['Birthday'] = contact['Birthday'].strftime('%m/%d/%Y')  # Fix here
                writer.writerow([contact['Name'], contact['Phone'], contact['Email'], contact['Birthday']])
        print("beep boop... saving...")
    except FileNotFoundError:
        print("BEEEEEEEP BOOOOOOOOOOP ERROR ERROR ERROR ERROR ERROR...NOOOOOOOOOOO")
        global greg
        greg = False
        return greg
    except AttributeError:
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone', 'Email', 'Birthday'])
            for contact in contacts.values(): # Loop through the contacts dictionary, the values are the inner dictionaries(how you deal with inner dictionaries)
                contact['Birthday'] = dt.datetime.strptime(contact['Birthday'], '%m/%d/%Y')
                contact['Birthday'] = contact['Birthday'].strftime('%m/%d/%Y')  # Fix here
                writer.writerow([contact['Name'], contact['Phone'], contact['Email'], contact['Birthday']])
        
def did_it_save(greg)-> bool:
    """summery:
    Tells the user if the contacts were saved or not.

    args:
       greg (bool): A boolean value indicating whether the contacts were saved or not.

    returns:
        bool: True if the contacts were saved, False otherwise.
    
    """
    try:
        if greg == True:
            print("Contacts saved successfully.")
            return True
        else:
            print("Contacts not saved.")
            return False
    except ValueError:
        print("Error: cannot save contacts due to ValueError")
        return False



question = ""
filename = ""

#-------------------------------------------------------------------------------------
def leave():
    """Summery:
    Asks the user if they want to leave the program.  Will automatically save the contacts to a csv file if the user says yes.
    You cannot escape the program without saving, although what you save it to is up to you.
    uses code from the save_csv() and save_csv_action() funtions in a way that exits the while loop.
    Makes use of the FileNotFoundError exception to exit the funtion and go to main menu in a amusing way.

    global varibles used:
        imput
        the_filename
        question
        contacts
    
        
    
    Args:
        None
    
    Returns:
        None
    """
    global imput
    global the_filename
    question = ""
    the_filename = ""
    global contacts
    try:
        question = input("Would you like to quit and save the contacts to a csv file? (y/n): ")
        question_choice= ['y', 'n', 'Y', 'N']   
        while question not in question_choice:
            question = input("Would you like to quit and save the contacts to a csv file? (y/n): ")
        if question == 'n':
            print("Contacts not saved.")
            raise FileNotFoundError
        elif question == 'y':
            the_filename = input("Enter the filename to save the contacts to: ")
            with open(the_filename, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Phone', 'Email', 'Birthday'])
                for contact in contacts.values(): # Loop through the contacts dictionary, the values are the inner dictionaries(how you deal with inner dictionaries)
                    contact['Birthday'] = contact['Birthday'].strftime('%m/%d/%Y')  # Fix here
                    writer.writerow([contact['Name'], contact['Phone'], contact['Email'], contact['Birthday']])
            print("beep boop... saving...")
            print("goodbye")
            quit()
    except FileNotFoundError:
        print("BEEEEEEEP BOOOOOOOOOOP ERROR ERROR ERROR ERROR ERROR...NOOOOOOOOOOO")
        return None
    except ValueError:
        print("Error: cannot save contacts due to ValueError")
        return None


# def save_csv_action(filename):

#     global greg
#     try:
#         with open(filename, 'w', encoding='utf-8', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(['Name', 'Phone', 'Email', 'Birthday'])
#             for contact in contacts.values(): # Loop through the contacts dictionary, the values are the inner dictionaries(how you deal with inner dictionaries)
#                 contact['Birthday'] = contact['Birthday'].strftime('%m/%d/%Y')  # Fix here
#                 writer.writerow([contact['Name'], contact['Phone'], contact['Email'], contact['Birthday']])
#         print("beep boop... saving...")
#     except FileNotFoundError:
#         print("BEEEEEEEP BOOOOOOOOOOP ERROR ERROR ERROR ERROR ERROR...")
#         global greg
#         greg = False
#         return greg





#################3


# The main function will be used to run the program. The main function will use a while loop to display the menu and get the user's choice. The main function will call the appropriate function based on the user's choice. The main function will also call the save_csv function to save the contacts to the csv file before the program ends.


def main():
    
    """A menu driven program that allows the user to add, view, delete, and view next birthday of contacts from a excel file of contacts."""
    import csv
    import datetime as dt
    import time
    contacts = {}
    contacts = import_csv("contacts.csv")  

    #Global varibles:
    # global varibles:
    wilson = True
    while wilson == True:
        NAME = ""
        PHONE = "" 
        EMAIL = ""
        BIRTHDAY = ""
        FIRST_THREE = ""
        SECOND_THREE = ""
        LAST_FOUR = ""
        DO_I_DELETE_CONTACT = bool()
        WALDO = ""
        print("Welcome to the Contact List Program")
        print("please choose from the following options below: ")
        print("--------------------------------------------------")
        print("press 1 to Add contact")
        print("press 2 to View contacts")
        print("press 3 to Delete contact")
        print("press 4 to Save contacts to csv file")
        print("press 5 to Next Birthday")
        print("press 6 to view contacts with pandas (Warning: will load slower)")
        print("press 0 to Quit")
        print("--------------------------------------------------")
        print("\n")
        imput = input("Please enter your choice: ")
        imput_list = ["0", "1", "2", "3", "4", "5", "restart","6"]
        while imput not in imput_list:
            print("Invalid input")
            imput = input("Please enter your choice: ")
        if imput == "restart":
            print("Welcome to the Contact List Program")
            print("please choose from the following options below: ")
            print("--------------------------------------------------")
            print("press 1 to Add contact") 
            print("press 2 to View contacts")
            print("press 3 to Delete contact")
            print("press 4 to Save contacts to csv file")
            print("press 5 to Next Birthday")
            print("press 6 to view contacts with pandas (Warning: will load slower)")
            print("press 0 to Quit")
            print("--------------------------------------------------")
            print("\n")
            imput = input("Please enter your choice: ")
        elif imput == "1":
            print("Add contact has been selected")
            get_contact_info()
            add_contact(NAME, PHONE, EMAIL, BIRTHDAY)
            print("\nremember to save after entering a contact, or it will be overwritten.\n")
            imput = "restart"
        elif imput == "2":
            print("View contacts has been selected")
            view_contacts()
            imput = "restart"
        elif imput == "3":
            print("Delete contact has been selected")
            get_name()
            global question
            question = delete_contact(NAME) #should i pop this instead???
            delete_contact_action(question)
            imput = "restart"
        elif imput == "4":
            print("Save contacts has been selected")
            global the_filename
            global greg
            greg = True
            question = ""
            the_filename = ""
            save_csv()
            # greg = save_csv(the_filename)
            save_csv_action(the_filename)
            did_it_save(greg)
            question = ""
            the_filename = ""
            imput = "restart"
        elif imput == "5":
            print("Look up next birthday has been selected")
            today = dt.date.today()
            next_birthday()
            imput = "restart"
        elif imput == "0":
            print("Quit has been selected")
            leave()
            print("heading back to the main menu")
            imput = "restart"
        elif imput == "6":
            print("View contacts with pandas has been selected")
            print("downloading pandas...please wait...")
            panda_display()
            imput = "restart"
        else:
            print("Invalid input")
            print("returning to the main menu")
            imput = "restart"

    #pass  # Remove this line when you start writing your code

    # After you are done with the program, answer the following questions using code (show your code and output):
    # How many names start with the letter A?
count = 0
for name in contacts.keys(): # loop through the keys in the dictionary, names are the keys
    if name.startswith('A'): # if the name starts with A... didn't even know .startswith was a thing
        count += 1
print(f'{count} is the number of names that start with the letter A')
    # How many emails are yahoo emails?
yahoo_count = 0
yahoo_list = []
for contact in contacts.values():# loop through the values in the dictionary, including the inner dictionaries
    yahoo_list.append(contact['Email']) # append the emails in the dictionary to the list
yahoo_list = ' '.join(yahoo_list) # convert the list to a string
yahoo_count = yahoo_list.count('yahoo.com') # count the number of times yahoo.com appears in the string
print(f'{yahoo_count} is the number of emails that end with yahoo.com')

    # How many .org emails are there?
org_count = 0
email_list = []
for contact in contacts.values():# loop through the values in the dictionary, including the inner dictionaries
    email_list.append(contact['Email']) # append the emails in the dictionary to the list
email_list = ' '.join(email_list) # convert the list to a string
org_count = email_list.count('.org') # count the number of times .org appears in the string
print(f'{org_count} is the number of emails that end with .org')


        
#     if email.endswith('.org'):
#         org_count += 1
# print(f'{org_count} is the number of emails that end with .org')

keys=contacts.keys()
# print(keys)



# How many contacts have a birthday in January?
jan_count = 0
for contact in contacts.values():
    if contact['Birthday'].month == 1:
        jan_count += 1
print(f'{jan_count} is the number of contacts that have a birthday in January')

    # How many contacts have a birthday in February?
feb_count = 0
for contact in contacts.values():
    if contact['Birthday'].month == 2:
        feb_count += 1
print(f'{feb_count} is the number of contacts that have a birthday in February')
if __name__ == "__main__":
    main()
