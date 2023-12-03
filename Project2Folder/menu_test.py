

# def mains():
#         print("Welcome to the Contact List Program")
#         print("please choose from the following options below: ")
#         print("--------------------------------------------------")
#         print("press 1 to Add contact")
#         print("press 2 to View contacts")
#         print("press 3 to Delete contact")
#         print("press 4 to Save contacts to csv file")
#         print("press 5 to Next Birthday")
#         print("press 0 to Quit")
#         print("--------------------------------------------------")
#         print("\n")
#         imput = input("Please enter your choice: ")




#         # if imput != 0 or imput != 1 or imput != 2 or imput != 3 or imput != 4 or imput != 5 or imput != "restart":
#         #     print("Invalid input")
#         # if imput == 0:
#         #     print("Goodbye")
#         # if imput == 1:
#         #     print("Add contact")    
#         # if imput == 2:  
#         #     print("View contacts")
#         # if imput == 3:
#         #     print("Delete contact")
#         # if imput == 4:
#         #     print("Save contacts to csv file")
#         # if imput == 5:
#         #     print("Next Birthday")
#         # if imput == "restart":
#         #      print("Restarting")
             
          

def mains():
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
    samantha = True
    while samantha == True:
        imput = input("Please enter your choice: ")

        if imput == "0":
            print("Goodbye")
            break
        elif imput == "1":
            print("Add contact")
            break
        elif imput == "2":
            print("View contacts")
            break
        elif imput == "3":
            print("Delete contact")
            break
        elif imput == "4":
            print("Save contacts to csv file")
            break
        elif imput == "5":
            print("Next Birthday")
            samantha
        else:
            print("Invalid input")

mains()