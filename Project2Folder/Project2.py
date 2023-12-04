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
        


                #finding something
#                name_lower = name.lower()
                #birthday = dt.datetime.strptime(row[3], '%m/%d/%Y') # 
#                contacts[name_lower] = {'Name': name,'Phone': phone, 'Email': email, 'Birthday': birthday} 
#
#

# contacts = {
#     'John': {
#         'Phone': '1234567890',
#         'Email': 'john@example.com',
#         'Birthday': '01/01/2000'
#     }
# }

# # Iterate over the outer dictionary
# for key, value in contacts.items():
#     # Check if the value is a dictionary
#     if isinstance(value, dict):
#         # Access the inner dictionary
#         inner_dict = value
#         print(inner_dict)
#         # Access specific values within the inner dictionary
#         phone = inner_dict.get('Phone')
#         email = inner_dict.get('Email')
#         birthday = inner_dict.get('Birthday')
#         print(phone)
#         print(email)
#         print(birthday)

#we just created a dictionary of dictionaries, the key is the name, the value is a dictionary of the  name, phone, email, and birthday

#contacts = the dictionary now
contacts = import_csv("contacts.csv")    
# print(contacts)

# Skip the first line of the csv file since it contains the column headers
# i can use next() to skip the first line
############################################################
# -------------------------------------------------------------------------------------

# add_contact(name, phone, email, birthday) - This function will add a contact to the dictionary. 
# The function will take four parameters, the name, phone number, email address, and birthday.
#  The function will return True if the contact was added and False if the contact was not added. 
# The function will display an error message if the contact already exists.
# Hint 1: You will need to convert the birthday to a datetime object.
#  You can do that by using the strptime function. IE. dt.datetime.strptime(birthday, '%m/%d/%Y')
# Hint 2: To add a contact to the dictionary, you need to use the key as the name and the values as a 
# dictionary that contains the phone number, email address, and birthday. To reference the specific key you can use contact[name]

# global variables:
NAME = ""
PHONE = ""
EMAIL = ""
BIRTHDAY = ""
WALDO = ""


def get_name():
    """
    Get the name from the user.
    """
    global NAME
    try:
        NAME = input("Enter name, This is case sensitive : ")
        return NAME
    except ValueError:
        print("Error: cannot add contact due to ValueError")
        NAME = input("Enter name, This is case sensitive : ")

FIRST_THREE = ""
SECOND_THREE = ""
LAST_FOUR = ""

def first_three_fun():
    """
    Get the first three digits of the phone number from the user.
    """
    global FIRST_THREE
    print(" I will need the phone number in the following format: 123-456-7890")
    try:
        FIRST_THREE = input("Enter the first three digits of the phone number: ")
        if not FIRST_THREE.isdigit() or len(FIRST_THREE) != 3:
            print("Invalid input, please try again")
            FIRST_THREE = input("Enter the first three digits of the phone number: ")
        return FIRST_THREE
    except ValueError:
        print("Error: lets try that again")

def second_three_fun():
    """
    Get the second three digits of the phone number from the user.
    """
    global SECOND_THREE
    try:
        SECOND_THREE = input("Enter the second three digits of the phone number: ")
        if not SECOND_THREE.isdigit() or len(SECOND_THREE) != 3:
            print("Invalid input, lets try that again")
            SECOND_THREE = input("Enter the second three digits of the phone number: ")
        return SECOND_THREE
    except ValueError:
        print("Error: lets try that again")
    # Not sure if value error will work here

def last_four_fun():
    """
    Get the last four digits of the phone number from the user.
    """
    global LAST_FOUR
    try:
        LAST_FOUR = input("Enter the last four digits of the phone number: ")
        if not LAST_FOUR.isdigit() or len(LAST_FOUR) != 4:
            print("Invalid input, lets try that again")
            LAST_FOUR = input("Enter the last four digits of the phone number: ")
        return LAST_FOUR
    except ValueError:
        print("Error: lets try that again")

def get_phone():
    """
    Get the phone number from the user.
    """
    global PHONE
    global FIRST_THREE
    global SECOND_THREE
    global LAST_FOUR
    first_three_fun()
    second_three_fun()
    last_four_fun()
    PHONE = FIRST_THREE + "-" + SECOND_THREE + "-" + LAST_FOUR
    return PHONE



def get_email():
    global EMAIL
    try:
        EMAIL = input("Enter email: ")
        if "@" in EMAIL and "." in EMAIL:
            return EMAIL
        else:
            print("Invalid email, please try again")
            EMAIL = input("Enter email: ")
    except ValueError:
        print("Error: cannot add contact due to ValueError")




def get_birthday():
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





def get_contact_info():
    global NAME
    global PHONE
    global EMAIL
    global BIRTHDAY
    get_name()
    get_phone()
    get_email()
    get_birthday()
    contacts[NAME] = {'Name': NAME, 'Phone': PHONE, 'Email': EMAIL, 'Birthday': BIRTHDAY}
    return contacts[NAME]

def add_contact():
    try:
        if NAME in contacts:
            print("Error: Contact already exists")
            return False
        elif NAME not in contacts:
            contacts[NAME] = {'Name': NAME, 'Phone': PHONE, 'Email': EMAIL, 'Birthday': BIRTHDAY}
            return True
        else:
            print("Error: cannot add contact due to ValueError")
            return False
    except ValueError:
        print("Error: cannot add contact due to ValueError")
        return False

#------------------------




# def add_contact(name, phone, email, birthday) -> bool:
#     """ returns true if contact was added, false if not"""
#     global contacts
#     try:
#         if name in contacts:
#             print("Error: Contact already exists")
#             return False
#         elif name not in contacts: 
#             contacts[name] = {'Name': name, 'Phone': phone, 'Email': email, 'Birthday': birthday}
#             WALDO = True
#             return True    
#     except ValueError:
#         print("Error: cannot add contact due to ValueError")
#         return False 
#________________________________________________________________________________
#waldo = add_contact(name, phone, email, birthday)
#________________________________________________________________________________
# new_name = ""
# def put_contact_together(name, phone, email, birthday):
#     global contracts
#     contacts[name] = { 
#     'Name': name,
#     'Phone': phone,
#     'Email': email,
#     'Birthday': birthday
    

#contact is a list of dictionaries, with the key being the name, and the value being a dictionary of the name, phone, email, and birthday


# def add_contact(name, phone, email, birthday) -> bool:
#     """ returns true if contact was added, false if not"""
#     global contacts
#     phone
#     email
#     birthday
#     try:

#         if name in key_list:
#             print("Error: Contact already exists")
#             return False
#         if name in contacts:
#             print("contact sucessfully added")
#             return True
#         elif name not in contacts:  
#             return False
#     except ValueError:
#         print("Error: cannot add contact due to ValueError")
#         return False 
""" 
def add_keys(name):
    global keys
    keys.append(name)
    keys = contacts.keys()
    return keys
"""
#in code
def reset_variables():
    global NAME
    global PHONE
    global EMAIL
    global BIRTHDAY
    global DO_I_DELETE_CONTACT
    global FIRST_THREE
    global SECOND_THREE
    global LAST_FOUR
    global WALDO
    NAME = ""
    PHONE = ""
    EMAIL = ""
    BIRTHDAY = ""
    DO_I_DELETE_CONTACT = ""
    FIRST_THREE = ""
    SECOND_THREE = ""
    LAST_FOUR = ""
    WALDO = ""

##################################



#-------------------------------------------------------------------------------------

#2.) view_contacts() - This function will display the contacts in the dictionary. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. Use string formatting to display the contacts in a table format. The table should have a header row and each contact should be on a separate row. The table should have the following columns: Name, Phone, Email, Birthday. The birthday should be formatted as mm/dd/yyyy. The table should be sorted by name.

def view_contacts():
    """
    Display the contacts in the dictionary in a table format.
    """
    global contacts

    if len(contacts) == 0:
        print("There are no contacts in the dictionary.")
    else:
        print("Name\tPhone\tEmail\tBirthday")
        for name, contact in contacts.items():
            print(f'{name}\t{contact["Phone"]}\t{contact["Email"]}\t{contact["Birthday"]}')

# Hint 1: You will need to loop through the dictionary to display the contacts. IE. for key, value in contact.items():
# Extra Credit: The data is a dictionary of dictionaries. You can unpack the dictionary into a list of dictionaries. Like in Lab 10 and then use the tabulate library to display the contacts in a table format. This is optional and not required. You can use string formatting to display the contacts in a table format.

""" I think I got this done"""

#____----------------------------

# delete_contact(id) - This function will delete a contact from the dictionary. 
# The function will take one parameter, the name of the contact to delete.
#  The function will return True if the contact was deleted and False if the contact was not deleted.
#  The function will display an error message if the contact does not exist.
""" this is done for the most part, need to program  what happens"""
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
    except:
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
def save_question():
    global imput
    global the_filename
    question = input("Would you like to save the contacts to a csv file? (y/n): ")
    if question.lower() == 'y':
        the_filename = input("Enter the filename to save the contacts to: ")
        return the_filename
    else:
        print("Contacts not saved.")
        imput = "restart"
        return imput


# def save_csv(filename):
#     try:
#         with open(filename, 'w') as file:
#             writer = csv.writer(file)
#             writer.writerow(['Name', 'Phone', 'Email', 'Birthday'])
#             for contact in contacts.values():
#                 writer.writerow([contact['name'], contact['phone'], contact['email'], contact['birthday']])
#         return True
#     except:
#         return False



def save_csv_action(filename):
    try:
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone', 'Email', 'Birthday'])
            for contact in contacts.values(): # Loop through the contacts dictionary, the values are the inner dictionaries(how you deal with inner dictionaries)
                contact['Birthday'] = contact['Birthday'].strftime('%m/%d/%Y')  # Fix here
                writer.writerow([contact['Name'], contact['Phone'], contact['Email'], contact['Birthday']])
        print("beep boop... saving...")
    except FileNotFoundError:
        print("BEEEEEEEP BOOOOOOOOOOP ERROR ERROR ERROR ERROR ERRO")
        global greg
        greg = False
        return greg
        
def did_it_save(greg):
    if greg == True:
        print("Contacts saved successfully.")
    else:
        print("Contacts not saved.")
        return greg

question = ""
filename = ""

"""
question = None
filename = None
greg = None
save_question()
greg = save_csv(the_filename)
save_csv_action(greg)
question = None
filename = None
greg = None
imput = "restart"




"""
# The main function will be used to run the program. The main function will use a while loop to display the menu and get the user's choice. The main function will call the appropriate function based on the user's choice. The main function will also call the save_csv function to save the contacts to the csv file before the program ends.


def main():
    
    """Add Code here to call the functions and run the program"""
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
        print("press 0 to Quit")
        print("--------------------------------------------------")
        print("\n")
        imput = input("Please enter your choice: ")
        imput_list = ["0", "1", "2", "3", "4", "5", "restart",'list']
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
            print("press 0 to Quit")
            print("--------------------------------------------------")
            print("\n")
            imput = input("Please enter your choice: ")
        elif imput == "1":
            print("Add contact has been selected")
            get_contact_info()
            add_contact()
            print("\nremember to save after entering a contact, or it will be overwritten.\n")
            imput = "restart"
        elif imput == "2":
            print("View contacts has been selected")
            view_contacts()
            reset_variables()
            imput = "restart"
        elif imput == "3":
            print("Delete contact has been selected")
            get_name()
            global question
            question = delete_contact(NAME) #should i pop this instead???
            delete_contact_action(question)
            reset_variables()
            imput = "restart"
        elif imput == "4":
            print("Save contacts has been selected")
            global the_filename
            global greg
            greg = True
            question = ""
            the_filename = ""
            save_question()
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
            print("Thank you for using the Contact List Program")
            time.sleep(2)
            print("Goodbye")
            quit()
        elif imput == "list":
            print(contacts)
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
