#getTesting
name = ""
def get_name():
    global name
    try:
        name = input("Enter name, This is case sensitive : ")
        return name
    except ValueError:
        print("Error: cannot add contact due to ValueError")
        name = input("Enter name, This is case sensitive : ")
what= get_name()
print(what)