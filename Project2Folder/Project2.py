# Project 2
# Name:
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


                #finding something
#                name_lower = name.lower()
                #birthday = dt.datetime.strptime(row[3], '%m/%d/%Y') # 
#                contacts[name_lower] = {'Name': name,'Phone': phone, 'Email': email, 'Birthday': birthday} 
#
#



#we just created a dictionary of dictionaries, the key is the name, the value is a dictionary of the  name, phone, email, and birthday

#contacts = the dictionary now
contacts = import_csv("contacts.csv")    
print(contacts)

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

# global varibles:
name = ""
name_key = ""
phone = ""
email = ""
birthday = ""



def get_name():
    global name
    name = input("Enter name, This is case sensitive : ")
    return name

def lower_name_key():
    global name_key
    global name
    name_key = name.lower()
    return name_key

def get_phone():
    global phone
    print(" I will need the phone number in the following format: 123-456-7890")
    phone = input("Enter phone number: ")
    return phone


def get_email():
    global email
    email = input("Enter email: ")
    return email

def get_birthday():
    global birthday
    while True:
        try:
            birthday = input("Enter birthday in this format: (mm/dd/yyyy): ")
            dt.datetime.strptime(birthday, '%m/%d/%Y')
            break
        except ValueError:
            print("Invalid date format. Please enter the birthday in the format mm/dd/yyyy.")
    return birthday




def get_contact_info():
    global name
    global name_key
    global phone
    global email
    global birthday
    get_name()
    lower_name_key()
    get_phone()
    get_email()
    get_birthday()

    return name, name_key, phone, email, birthday


#------------------------




def add_contact(name, phone, email, birthday):
    global contacts
    try:
        if name in contacts:
            print("Error: Contact already exists")
            return False
        contacts[name] = {'Phone': phone, 'Email': email, 'Birthday': birthday}
        return True    
    except ValueError:
        print("Error: cannot add contact due to ValueError")
        return False 
#________________________________________________________________________________
waldo = add_contact(name, phone, email, birthday)
#________________________________________________________________________________

def add_contact_action(name, phone, email, birthday):
    global contacts
    if waldo == True:
        contacts[name] = {'phone': phone, 'email': email, 'birthday': birthday}
        print("Contact added successfully.")
        return contacts
    else:
        print("Contact not added.")
    return contacts

#in code
def reset_varibles():
    global name
    global name_key
    global phone
    global email
    global birthday
    global do_I_delete_contact
    name = ""
    name_key = ""
    phone = ""
    email = ""
    birthday = ""
    do_I_delete_contact = None
    return name, name_key, phone, email, do_I_delete_contact 

##################################



#-------------------------------------------------------------------------------------

#2.) view_contacts() - This function will display the contacts in the dictionary. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. Use string formatting to display the contacts in a table format. The table should have a header row and each contact should be on a separate row. The table should have the following columns: Name, Phone, Email, Birthday. The birthday should be formatted as mm/dd/yyyy. The table should be sorted by name.
# key = input("please enter a name.  This is case sensitive: ")
# for contacts, value in contacts.items():
#         if key == 'name' in contacts:
#             print(value)


def view_contacts():
    global contacts
    global imput
    if len(contacts) == 0:
        print("There are no contacts in the dictionary.")
        imput = "restart"
    else:
        
        print("Name\tPhone\tEmail\tBirthday")
        for name, contacts in contacts.items():
            print(f'{name}\t{contacts["Phone"]}\t{contacts["Email"]}\t{contacts["Birthday"].strftime("%m/%d/%Y")}')

# Hint 1: You will need to loop through the dictionary to display the contacts. IE. for key, value in contact.items():
# Extra Credit: The data is a dictionary of dictionaries. You can unpack the dictionary into a list of dictionaries. Like in Lab 10 and then use the tabulate library to display the contacts in a table format. This is optional and not required. You can use string formatting to display the contacts in a table format.

""" I think I got this done"""

#____----------------------------

# delete_contact(id) - This function will delete a contact from the dictionary. 
# The function will take one parameter, the name of the contact to delete.
#  The function will return True if the contact was deleted and False if the contact was not deleted.
#  The function will display an error message if the contact does not exist.
""" this is done for the most part, need to program  what happens"""
def delete_contact(do_I_delete_contact: bool)->bool:
    global contacts

    if name in contacts:
        #del contacts[name]
        return True
    else:
        print("Error: Contact does not exist")
        return False

def delete_contact_action():
    if do_I_delete_contact == True:
        try:
            name = get_name()
            del contacts[name]
            print("Contact deleted")
            return  contacts[name]
        except:
            print("Error: Contact does not exist")
    else:
        print("Contact not deleted")

#-------------------------------------------------------------------------------------
# next_birthday() - This function will display the next birthday. 
# The function will take no parameters. The function will return nothing.
#  The function will display a message if there are no contacts in the dictionary.
#  The function will display a message if there are no birthdays in the next 30 days.
#  The function will display the next birthday and name if there is a birthday in the next 30 days.
#  Use string formatting to display the next birthday.
#  The next birthday should be sorted by the next birthday.
#  The next birthday should be formatted as mm/dd/yyyy.
# Hint: We dont care about the year, only the month and day.
#  There are many ways to solve this issue. 1st you could replace all the years with the current year.
# 2nd you could use the month and day attributes of the datetime object to compare the month and day of the birthday to the 
# current month and day.
import datetime as dt
today = ""
next_birthdays = ""
birthday = ""

def next_birthday():
    if not contacts:# not sure if this is needed
        print("No contacts in the dictionary.") # not sure if this is needed
        return #not sure if this is needed 
    global today
    global next_birthdays
    today = dt.date.today()
    next_birthdays = None
    
    for contact in contacts.values():
        birthday = contact.get('birthday')
        if birthday:
            birthday = dt.datetime.strptime(birthday, "%m/%d/%Y").date()
            birthday = birthday.replace(year=today.year)
            
            if birthday >= today and (next_birthday is None or birthday < next_birthday):
                next_birthdays = birthday
    
    if next_birthday is None:
        print("No birthdays in the next 30 days.")
    else:
        print("Next birthday: {}".format(next_birthday.strftime("%m/%d/%Y")))
 
def reset_birthday_varibles():
    global today
    global next_birthday
    global birthday
    today = ""
    next_birthday = ""
    birthday = ""
    return today, next_birthdays, birthday



#-------------------------------------------------------------------------------------
# save_csv(filename) - This function will save the contacts to the csv file. Prompt the user to enter a filename to save the contacts to. If the file exists, overwrite the file. If the file does not exist, create the file. The function will return True if the contacts were saved and False if the contacts were not saved.
question = None
the_filename = None
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


def save_csv(filename):
    try:
        with open(filename, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone', 'Email', 'Birthday'])
            for contact in contacts.values():
                writer.writerow([contact['name'], contact['phone'], contact['email'], contact['birthday']])
        return True
    except:
        return False



def save_csv_action(question):
        if question == True:
            with open(filename, 'w') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Phone', 'Email', 'Birthday'])
                for contact in contacts.values():
                    writer.writerow([contact['name'], contact['phone'], contact['email'], contact['birthday']])
            print("Contacts saved successfully.")
            return contacts
        else:  
            print("Contacts not saved.")
            return contacts
        
question = None
filename = None

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
    wilson = True
    while wilson == True:
        contacts = {}
        contacts = import_csv("contacts.csv")    
        #Global varibles:
        # global varibles:

        name = ""
        name_key = ""
        phone = "" 
        email = ""
        birthday = ""
        do_I_delete_contact = bool()
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
        imput_list = ["0", "1", "2", "3", "4", "5", "restart"]
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
            reset_varibles()
            get_contact_info()
            add_contact(name, phone, email, birthday)
            add_contact_action(name, phone, email, birthday)
            reset_varibles()
            print("returning to main menu")
            imput = "restart"
        elif imput == "2":
            print("View contacts has been selected")
            view_contacts()
            reset_varibles()
            imput = "restart"
        elif imput == "3":
            print("Delete contact has been selected")
            get_name()
            delete_contact(name) #should i pop this instead???
            delete_contact_action()
            reset_varibles()
            imput = "restart"
        elif imput == "4":
            print("Save contacts has been selected")
            global question
            global The_filename
            global greg
            question = None
            the_filename = None
            greg = None
            save_question()
            greg = save_csv(the_filename)
            save_csv_action(greg)
            question = None
            filename = None
            greg = None
            imput = "restart"

        elif imput == "5":
            print("Look up next birthday has been selected")
            next_birthday()
            reset_birthday_varibles()
            imput = "restart"
        elif imput == "0":
            print("Thank you for using the Contact List Program")
            time.sleep(2)
            print("Goodbye")
            quit()
        else:
            print("Invalid input")
            print("returning to the main menu")
            imput = "restart"

    #pass  # Remove this line when you start writing your code

    # After you are done with the program, answer the following questions using code (show your code and output):
    # How many names start with the letter A?

    # How many emails are yahoo emails?

    # How many .org emails are there?

    # How many contacts have a birthday in January?


if __name__ == "__main__":
    main()
