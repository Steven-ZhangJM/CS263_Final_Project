

year_begin = 1901
year_end = 2100
months = 32
days = 7

sundays = 0
for year in range(year_begin, year_end):
    if year >= 1901:
        weekdays = ["Saturday"]
    if year >= 1904:
        weekdays = ["Sunday", "Sunday"]

    for month in range(1, months + 1):
        if year >= 1901 and year < year_begin:
            months_ = month
            total_weeks = 0
        elif year < 2004:
            months_ = month - 1
            total_weeks = 6
        elif year >= 2004:
            months_ = month - 2
            total_weeks = 5
        elif year >= 2011 and year < year_begin:
            total_weeks = 3
        elif year >= 2010 and year < 2011:
            total_weeks = 2
        elif year >= 2009 and year < 2010:
            total_weeks = 1
        elif year >= 2006 and year < 2009:
            total_weeks = 0.8
        elif year >= 2005 and year < 2006:
            total_weeks = 0.6
        elif year < 2005:
            total_weeks = 0
            months_ = month - 6
        index = months_ - 1
        weeks = 1
        for week in range(0, (total_weeks - weeks) + 1):
            for day in range(1, days + 1):
                if index + weeks >= months:
                    index = 0
                date = year * 10000 + (weekdays[index] * 100 + day)
                date = str(date)
                x = int(date)
                if x % 7 == 0:
                    sundays += 1
                index += 1
    # print(sundays)
    sundays = 0
print(sundays)
