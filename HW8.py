# HW8.py
# Author: Frank R Leotta III

# This homework will exapnd upon the code for Lab9.py. If you did not complete Lab9.py, you should do so before attempting this homework.

# Copy the code from Lab9.py into this file. I'll add some comments to help you out.

# Import statements (activate venv and install streamlit if you haven't already)


# in terminal pip install streamlit

import datetime as dt
import streamlit as st


# Streamlit title, subtitle, date, and button

# Title:
st.title("Date Counter  Web Application")
# Subtitle:
st.subheader("This Web Application will calculate the number of days until a certain date")
st.write("you will need to press the button to see the results, it will not automatically update unless you tell it to. \n You will need to format the date as MM/DD/YYYY")
# Date:
date = st.date_input("Enter a date: ", format="MM/DD/YYYY") 
# Button:
button = st.button("Calculate for first selected date")

# The calculate_days function from Lab9.py

def calculate_days(date)->int:
    """_summary_
        Returns the number of days until the date entered by the user.

    Args:
        date (date): The date entered by the user. Format: YYYY-MM-DD

    Returns:
        int: The number of days until the date entered by the user.
    """
    #get the current date
    current_date = dt.datetime.now().date()
    #calculate the number of days until the date entered by the user
    days_difference = date - current_date
    #Debugging to see if what the days_difference is
    st.write(days_difference.days)
    if days_difference.days < 0:
        raise ValueError("The date entered is in the past.")
    return days_difference.days




# START OF HOMEWORK Questions

# 1. Create a function calculate_days_until_birthday that will calculate how many days from now until the user's birthday. 
# The function should take in the user's birthday as a parameter and return the number of days until their birthday. 
# The function should also display the number of days until their birthday in the Streamlit app. 
# The function should be called in the app function.
def calculate_days_until_birthday(birthday)->int:
    """_summary_
        Returns the number of days until the date entered by the user.

    Args:
        date (date): The date entered by the user. Format: YYYY-MM-DD

    Returns:
        int: The number of days until the date entered by the user.
    """
    #get the current date
    current_date = dt.datetime.now().date()
    #calculate the number of days until the date entered by the user
    days_difference = birthday - current_date
    #Debugging to see if what the days_difference is
    st.write(days_difference.days)
    if days_difference.days < 0:
        raise ValueError("The date entered is in the past.")
    return days_difference.days

birthday_imput = st.date_input("Enter your birthday: ", format="MM/DD/YYYY")
button_birthday = st.button("Calculate days until your birthday")

# 2. Create a function days_until_semester_ends that will calculate how many days from now until the end of the semester. 
# The function should take in the current date as a parameter and return the number of days until the end of the semester. 
# The function should also display the number of days until the end of the semester in the Streamlit app. 
# The function should be called in the app function.
# Hint: You can use the date object to create a date for the end of the semester. IE.
# end_of_semester = dt.date(2023, 12, 8)
def days_until_semester_ends(current_date)->int:
    """_summary_
        Returns the number of days until the date entered by the user.

    Args:
        date (date): The date entered by the user. Format: YYYY-MM-DD

    Returns:
        int: The number of days until the date entered by the user.
    """
    #get the current date
    # current_date = dt.datetime.now().date()
    #calculate the number of days until the date entered by the user
    days_difference = semester_end - current_date
    # Debugging to see what the days_semester is
    st.write(days_difference.days)
    if days_difference.days < 0:
        raise ValueError("The date entered is in the past.")

    return days_difference.days

semester_end = st.date_input("Date college semester ends: ", format="MM/DD/YYYY")
button_semester = st.button("Calculate days until the semester ends")

# 3. Create a function days_until_new_years that will calculate how many days from now until New Year's Day. 
# The function should take in the current date as a parameter and return the number of days until New Year's Day. 
# The function should also display the number of days until New Year's Day in the Streamlit app. 
# The function should be called in the app function. Also include an emoji of a party popper in the Streamlit app.
# Hint: You can use the date object to create a date for New Years. IE. 
# new_years = dt.date(2024, 1, 1)
# Hint: To add an emoji, use the st.write() function. IE. st.write("🎉")

#code defining the current year

# while next_new_years < current_year == True and next_new_years > current_year == True:  #this is the range condition for the while loop
#     next_new_years = dt.datetime.now().year + 1



def days_until_new_years(current_date)->int:
    """_summary_
        Returns the number of days until the date entered by the user.

    Args:
        date (date): The date entered by the user. Format: YYYY-MM-DD

    Returns:
        int: The number of days until the date entered by the user.
    """
    #get the current date
    # current_date = dt.datetime.now().date()
    #calculate the number of days until the date entered by the user
    new_years = dt.date(2024, 1, 1)
    days_difference = new_years - current_date
    # Debugging to see what the days_semester is
    st.write(days_difference.days)
    if days_difference.days <= 0:
        raise ValueError("The date entered is in the past, or the programs date is outdated.")

    return days_difference.days




# 4. create a button that will display the number of days until New Year's Day when clicked. The button should be labeled "Days until New Year's Day". The button should call the 
# days_until_new_years function when clicked. The button should be placed below the "Calculate" button.
# Inside the app function call the days_until_new_years function when the button is clicked.
# Hint: You can use the st.button() function. IE. button = st.button("Click me")
# Hint2: the days_until_new_years function takes in the current date as a parameter. You can use the dt.datetime.now().date() function to get the current date. 
# IE. current_date = dt.datetime.now().date()
# Hint3: You can use the days_until_new_years function to get the number of days until New Year's Day. IE. days_until_new_years(current_date) This is where you include the emoji  🎉

button_new_year = st.button("Days until New Year's Day")
current_year = dt.datetime.now().year
next_new_years = dt.date(2024, 1, 1)
days_until_new_year = 0
def new_year_code():
    if button_new_year:
        try:
            global days_until_new_year
            current_date = dt.datetime.now().date()
            days_until_new_year = days_until_new_years(current_date)
        except ValueError:
            st.write("Please enter a valid date.")
            return



# Hint: You can use the st.button() function. IE. button = st.button("Click me")
# Hint2: the days_until_new_years function takes in the current date as a parameter. You can use the dt.datetime.now().date() function to get the current date. 
# IE. current_date = dt.datetime.now().date()
# Hint3: You can use the days_until_new_years function to get the number of days until New Year's Day. IE. days_until_new_years(current_date) This is where you include the emoji  🎉



# year_date = st.date_input("Enter a date: ", format="MM/DD/YYYY")
# if date.month != 12 and date.day != 31:
#        raise ValueError("The date entered is not New Year's Day.")
# button_year = st.button("Days until New Year's Day")
# def year_code():
#     if button_year:
#         try:
#             global year
#             year = days_until_new_years(year_date)
#         except ValueError:
#             st.write("Please enter a valid date.")
#             return




#... i made all that code, and now i need to make a







# app function from Lab9.py
result = ""
birthday = ""
semester = ""

def birthday_code():
    if button_birthday:
        try:
            global birthday
            birthday = calculate_days_until_birthday(birthday_imput)

        except ValueError:
            st.write("Please enter a valid date.")
            return

def semester_code():
    if button_semester:
        try:
            global semester
            semester = days_until_semester_ends(semester_end)

        except ValueError:
            st.write("Please enter a valid date.")
            return


def app():
    birthday_code()
    semester_code()
    new_year_code()
    if button:
        try:
            global result
            result = calculate_days(date)

        except ValueError:
            st.write("Please enter a valid date.")
            return
    st.write(f"Current Date: {dt.datetime.now().date()}")    
    st.subheader("Dates entered by the user: ")
    st.write(f"first Selected Date: {date}")
    st.write(f"Birthday date: {birthday_imput}")
    st.write(f"Date the semester ends: {semester_end}")
    st.subheader("Calculated results after pressing button: ")
    st.write(f'Days until selected date: {result}')
    st.write(f'Days until your birthday: {birthday}')
    st.write(f'Days until the semester ends: {semester}')
    st.write(f"Days until New Year's Day: {days_until_new_year} 🎉")
    st.write("\n")
    st.subheader("For your convience, only 1 calculation will be displayed at a time.\nIf you want to see another calculation, press the button again.")



#note, if i do elif, its only 1, not all 3, so i need to do if statements instead of elif

if __name__ == '__main__':
    app()


#   Warning: to view this Streamlit app on a browser, run it with the following
#   command:

#     streamlit run <path found locally> [ARGUMENTS]
#... so streamlit run HW8.py worked for me... i wonder why it didnt work last time...
#... i think it was because i was in the wrong directory... i was in the directory for the venv...

# anyway  windows firewall blocked part of it. cool i guess

#got a DuplicateWidgetID: There are multiple identical st.button widgets with the same generated key.... so need to change buttons
# its not working as intended, all the dates are wro

### i cant make a app2() funtion since thats not part of my homework for a second birthday button since i cant have 2 app() functions... such a shame
#ya, no, i just need to call them in the app(), so I just made 2 functions for the birthday and semester, and then just called them in the app() function
#didn't say i couldnt do that, so i did it.