# Name: Write a function
# Problem: https://www.hackerrank.com/challenges/write-a-function/problem
# Score: 10

def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0 and not year % 400 == 0:
            leap = False
    return leap
