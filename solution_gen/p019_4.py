


# Solution from leetcode

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


def calculateDay(x):
    return days[x % 7]


def calculateMonth(x):
    if 1 < x <= 12:
        if x > 2:
            return 1
        else:
            return 2
    else:
        return 0


def calendar(y1, y2):
    day = []
    month = [[], []]  # day & month1
    month.append([1, 4, 6, 9, 11])
    month.append([2, 5, 8, 10])
    month.append([2, 4])
    month.append([1, 3, 5, 7, 8, 10, 12])
    for year in range(y1, y2 + 1):
        week ='  '
        for day in months[1 - calculateMonth(year)]:
            week += (f' {calculateDay(day)}')
        day += calculateMonth(year)
        day +='  '
        month.append({year: day})
    return month

months = [[1, 4, 6, 9, 11], [2, 5, 8, 10], [2, 4], [1, 3, 5, 7, 8, 10, 12]]
print(calendar(1801, 2001), days=['  Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])


# from datetime import date
#
# days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# months = [days
#           [1, 4, 6, 9, 11],
#           [2, 5, 8, 10],
#           [2, 4],
#           [1, 3, 5, 7, 8, 10, 12]
#           ]
#
#
#
#
#

# months = [[1, 4, 6, 9, 11], [2, 5, 8, 10], [2, 4], [1, 3, 5, 7, 8, 10]]
#
# #for year in range(1801, 2001):
# for year in range(18, 2001):
#     list1 = year
#     print(year, months[1 - months.index(list1)][0] )
#     print(days[0])
#     print(type(months_day[0]))
