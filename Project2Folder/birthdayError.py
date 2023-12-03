#birthdayError
import csv
import datetime as dt
import time

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

name = ""
phone = ""
email = ""
birthday = ""
waldo = None


def get_name():
    global name
    try:
        name = input("Enter name, This is case sensitive : ")
        return name
    except ValueError:
        print("Error: cannot add contact due to ValueError")
        name = input("Enter name, This is case sensitive : ")

first_three = ""
second_three = ""
last_four = ""

def first_three_fun():
    global first_three
    print(" I will need the phone number in the following format: 123-456-7890")
    try:
        global first_three
        first_three = input("Enter the first three digits of the phone number: ")
        if not first_three.isdigit() or len(first_three) != 3:
            print("Invalid input, please try again")
            first_three = input("Enter the first three digits of the phone number: ")
        return first_three
    except ValueError:
        print("Error: lets try that again")

def second_three_fun():
    global second_three
    try:
        global second_three
        second_three = input("Enter the second three digits of the phone number: ")
        if not second_three.isdigit() or len(second_three) != 3:
            print("Invalid input, lets try that again")
            second_three = input("Enter the second three digits of the phone number: ")
        return second_three
    except ValueError:
        print("Error: lets try that again")
    # Not sure if value error will work here

def last_four_fun():
    global last_four
    try:
        global last_four
        last_four = input("Enter the last four digits of the phone number: ")
        if not last_four.isdigit() or len(last_four) != 4:
            print("Invalid input, lets try that again")
            last_four = input("Enter the last four digits of the phone number: ")
        return last_four
    except ValueError:
        print("Error: lets try that again")

def get_phone():
    global phone
    global first_three
    global second_three
    global last_four
    first_three_fun()
    second_three_fun()
    last_four_fun()
    phone = first_three + "-" + second_three + "-" + last_four
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
    birthday = dt.datetime.strptime(birthday, '%m/%d/%Y')
    return birthday


def reset_variables():
    global name
    global phone
    global email
    global birthday
    global do_I_delete_contact
    global first_three
    global second_three
    global last_four
    global waldo
    name = ""
    phone = ""
    email = ""
    birthday = ""
    do_I_delete_contact = ""
    first_three = ""
    second_three = ""
    last_four = ""
    waldo = ""

def get_contact_info():
    global name
    global phone
    global email
    global birthday
    get_name()
    get_phone()
    get_email()
    get_birthday()

    return name, phone, email, birthday



def add_contact(name, phone, email, birthday) -> bool:
    """ returns true if contact was added, false if not"""
    global contacts
    global waldo
    try:
        if name in contacts:
            print("Error: Contact already exists")
            return False
        else: 
            contacts[name] = {'Phone': phone, 'Email': email, 'Birthday': birthday}
            waldo = True
            return True    
    except ValueError:
        print("Error: cannot add contact due to ValueError")
        return False 
#________________________________________________________________________________
#waldo = add_contact(name, phone, email, birthday)
#________________________________________________________________________________

def add_contact_action(name, phone, email, birthday):
    """
    Add a contact to the contacts dictionary.
    """
    global contacts
    global waldo
    if waldo is True:
        contacts[name] = {'Name': name, 'Phone': phone, 'Email': email, 'Birthday': birthday}
        print("Contact added successfully.")
    else:
        print("Contact not added.")
    return contacts

#in code
def reset_variables():
    global name
    global phone
    global email
    global birthday
    global do_I_delete_contact
    global first_three
    global second_three
    global last_four
    global waldo
    name = ""
    phone = ""
    email = ""
    birthday = ""
    do_I_delete_contact = ""
    first_three = ""
    second_three = ""
    last_four = ""
    waldo = ""

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
        name = ""
        phone = "" 
        email = ""
        birthday = ""
        first_three = ""
        second_three = ""
        last_four = ""
        do_I_delete_contact = bool()
        waldo = None
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
            waldo = add_contact(name, phone, email, birthday)
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

    #pass  # Remove this line when you start writing 

if __name__ == "__main__":
    main()
