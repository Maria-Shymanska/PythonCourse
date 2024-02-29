from datetime import datetime

def get_days_from_today(date):
    # We get the current date without hours, minutes and seconds
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    # Break the line with the date into year, month and day
    year, month, day = map(int, date.split('-'))

    # Create a datetime object for a given date
    specified_date = datetime(year, month, day)

    # Calculate the difference in days and return it
    days_difference = (today - specified_date).days
    
    return days_difference