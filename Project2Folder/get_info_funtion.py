#getinfo
#first part prerequisit
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

import_csv('contacts.csv')

for key in contacts:
    key_list = contacts.keys()

print (key_list)


# add_contact(name, phone, email, birthday) - This function will add a contact to the dictionary. 
# The function will take four parameters, the name, phone number, email address, and birthday.
#  The function will return True if the contact was added and False if the contact was not added.
#  The function will display an error message if the contact already exists.
# Hint 1: You will need to convert the birthday to a datetime object. You can do that by using the strptime function.
#  IE. dt.datetime.strptime(birthday, '%m/%d/%Y')
# Hint 2: To add a contact to the dictionary, you need to use the key as the name and the values as a dictionary that 
# contains the phone number, email address, and birthday. To reference the specific key you can use contact[name]



# input_name = input("Enter name: ")
# input_phone = input("Enter phone: ")
# input_email = input("Enter email: ")
# input_birthday = input("Enter birthday: ")
# imput_list = []
# imput_list = ({input_name}, {input_phone}, {input_email}, {input_birthday})
# print(imput_list)

print("Warning: you need to save after entering a contact, or it will be overwritten.")


def add_contact_code():
    input_name = ""
    input_phone = ""
    input_email = ""
    input_birthday = ""


    imput_name = input("Enter name, This is case sensitive : ")
    print(" I will need the phone number in the following format: 123-456-7890")
    try:
        FIRST_THREE = input("Enter the first three digits of the phone number: ")
        if not FIRST_THREE.isdigit() or len(FIRST_THREE) != 3:
            print("Invalid input, please try again")
            FIRST_THREE = input("Enter the first three digits of the phone number: ")
        return FIRST_THREE
    except ValueError:
        print("Error: lets try that again")



    input_phone = input("Enter phone: ")
    input_email = input("Enter email: ")
    input_birthday = input("Enter birthday: ")

def add_contact_code(name, phone, email, birthday):
    global list
    global contacts
    name
    phone
    email
    birthday
    for contacts in key_list:
        try:
            if input_name == contacts:
                print("Contact already exists.")
                return False
            else:
                return True
        except:
            print("Contact already exists.")
            return False
    switch = add_contact_code()
switch = add_contact_code(imput_name, input_phone, input_email, input_birthday)

    #contacts[name] = {'Name': name,'Phone': phone, 'Email': email, 'Birthday': birthday}
        

