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
                birthday= dt.datetime.strptime(row[3], '%m/%d/%Y')
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
print("------------------")
print(contacts)