import datetime

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        if is_leap_year(year):
            return 29
        else:
            return 28

sundays = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        date = datetime.datetime(year, month, 1)
        if date.weekday() == 6: # Sunday is the sixth day of the week (Monday is 0)
            sundays += 1

print(sundays)
#