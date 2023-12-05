#project 2 notes from project 2, scraps of code and notes not needed for final draft

        


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


# print(contacts)

# Skip the first line of the csv file since it contains the column headers
# i can use next() to skip the first line
############################################################

### this is all attempts at trying to get the csv file to work
# I think I lost a few years of my life trying to figure this out


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
#in code, unused and not needed
# def reset_variables():
#     global NAME
#     global PHONE
#     global EMAIL
#     global BIRTHDAY
#     global DO_I_DELETE_CONTACT
#     global FIRST_THREE
#     global SECOND_THREE
#     global LAST_FOUR
#     global WALDO
#     NAME = ""
#     PHONE = ""
#     EMAIL = ""
#     BIRTHDAY = ""
#     DO_I_DELETE_CONTACT = ""
#     FIRST_THREE = ""
#     SECOND_THREE = ""
#     LAST_FOUR = ""
#     WALDO = ""

##################################

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
