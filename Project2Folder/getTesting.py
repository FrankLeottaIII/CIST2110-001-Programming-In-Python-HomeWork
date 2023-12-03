#getTesting
import datetime as dt
birthday = ""
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

print(get_birthday())