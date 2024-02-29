'''
Write the function get_str_date(date) that will convert the date from the database in the ISO format '2021-05-27 17:08:34.149Z' 
as the following line 'Thursday 27 May 2021' - day of the week, day, month and year.
The function returns the converted value when it is called.
'''

from datetime import datetime

def get_str_date(date):
    date_time_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fZ')
    return date_time_obj.strftime('%A %d %B %Y')