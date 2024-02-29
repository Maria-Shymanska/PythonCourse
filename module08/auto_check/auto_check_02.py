'''
Write a function to determine the number of days in a particular month. 
Your function should take two parameters: month - the number of the month as an integer in the range
from 1 to 12 and year - a year consisting of four digits. 
Check if the function correctly handles the month of February of the leap year.
'''

from datetime import date

def get_days_in_month(month, year):
    start_of_the_month = date(year=year, month=month, day=1)
    if month == 12:
        start_of_the_next_month = date(year=year + 1, month=1, day=1)
    else:
        start_of_the_next_month = date(year=year, month=month + 1, day=1)
    return (start_of_the_next_month - start_of_the_month).days