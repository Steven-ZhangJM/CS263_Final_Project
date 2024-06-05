import datetime

count = 0
for year in range(1901, 2001):
    for month in [4, 6, 9, 11]:  # September, June, November and April have 30 days
        if datetime.date(year, month, 1).weekday() == 6:  # Sunday is the sixth day of the week
            count += 1

print(count)