import calendar

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2019, 12, 3))
print()

print(calendar.calendar(2019, 3))

day_of_the_week = calendar.weekday(2019, 12, 22)
print(day_of_the_week)

is_leap = calendar.isleap(2019)
print(is_leap)

how_many_leap_days = calendar.leapdays(2000, 2021)
print(how_many_leap_days)
