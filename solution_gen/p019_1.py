


from datetime import datetime

monthDays = {
    'Jan': ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31'],
    'Feb': ['28', '31', '30', '30', '31', '30', '31', '31', '30', '31', '30', '31'],
    'Mar': ['31', '29', '30', '31', '30', '31', '30', '31', '30', '31', '30', '31'],
    'Apr': ['30', '31', '30', '31', '30', '31', '30', '31', '30', '31', '30', '31'],
    'May': ['31', '30', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31'],
    'Jun': ['30', '31', '30', '31', '30', '31', '30', '31', '30', '31', '30', '31'],
    'Jul': ['31', '30', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31'],
    'Aug': ['31', '30', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31'],
    'Sep': ['30', '31', '30', '31', '30', '31', '30', '31', '30', '31', '30', '31'],
    'Oct': ['31', '30', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31'],
    'Nov': ['30', '31', '30', '31', '30', '31', '30', '31', '30', '31', '30', '31'],
    'Dec': ['31', '30', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
}


class Solution:
    def first_sunday(self):
        total_days = 20201
        now = datetime.now()
        current_day = now.day
        starting_day = current_day
        total_days += (starting_day - 1) // 7
        total_days += (starting_day - 1) % 7

        return total_days - (starting_day - 1) if total_days < 0 else total_days

    def days_in_range(self, start_day, end_day):
        total_days = list(monthDays.values())
        for month in [k for k, v in monthDays.items() if v[0]!= '30']:
            total_days = total_days[1:]
        new_total = ''.join([k for k in total_days[:4]] +
                            total_days[4:7] +
                            total_days[7:]).replace('30', '20')
        if start_day < self.first_sunday():
            diff = self.first_sunday() - start_day
            current_month = start_day + len(new_total)
            current_day = int(current_month / 31)
            week = (current_month - current_day * 31) % 7
            total = list(new_total)
            for i in range(diff):
                total.insert(week, '0')
        else:
            diff = end_day - self.first_sunday()
            current_month = end_day - len(new_total)
            current_day = int(current_month / 31)
            week = (current_month - current_day * 31) % 7
            if diff > 1:
                total = list(new_total)
                for i in range(diff - 1):
                    total.insert(week, '0')
            else:
                total = new_total + '0'
        return len(total)


test = 15

print(test, 'days')
s = Solution()
solution = s.days_in_range(15, 25)
print(solution)

