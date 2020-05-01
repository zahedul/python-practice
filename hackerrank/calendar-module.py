import calendar

month, day, year = map(int, input().split())
c = calendar.weekday(year, month, day)
print(calendar.day_name[c].upper())