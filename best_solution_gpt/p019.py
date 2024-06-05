import datetime

def count_sundays_on_first_of_month(start_year, end_year):
    # Count of Sundays that fell on the first of the month
    sunday_count = 0
    
    # Loop over each month of each year
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            # If the first day of the month is a Sunday
            if datetime.date(year, month, 1).weekday() == 6:
                sunday_count += 1
                
    return sunday_count

# Count the number of Sundays that fell on the first of the month during the 20th century
print(count_sundays_on_first_of_month(1901, 2000))