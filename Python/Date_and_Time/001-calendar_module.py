# Name: Calendar Module
# Problem: https://www.hackerrank.com/challenges/calendar-module/problem
# Score: 10


import calendar

month, day, year = list(map(int, input().split()))
print(calendar.day_name[calendar.weekday(year, month, day)].upper())
