#HW8_while_loop.py

import datetime as dt
import streamlit as st
current_date = dt.datetime.now().date()
current_year = dt.datetime.now().year
#current_year = 2020
new_year = dt.datetime.now().year + 1

while new_year < current_year and new_year > current_year:
    new_year += 1

print(new_year)
