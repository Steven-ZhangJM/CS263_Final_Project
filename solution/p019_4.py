def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(month, year):
    if month in [9, 4, 6, 11]:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 31

def first_sunday_of_month(month, year):
    days = [31, days_in_month(month, year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for day in range(days[month - 1]):
        if day % 7 == 0:  # Sunday
            return f"1 {calendar.month_name[month]} {year}"

# Initialize a list to store the first Sundays of each month
sundays = []

for year in range(1901, 2001):
    for month in range(1, 13):
        if day % 7 == 0:  # Sunday
            sundays.append(f"1 {calendar.month_name[month]} {year}")

print(len(sundays))
```
#