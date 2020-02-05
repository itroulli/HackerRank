# Name: Day 16: Exceptions - String to Integer
# Problem: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem
# Score: 30


import sys


S = input().strip()
try:
    print(int(S))
except ValueError:
    print("Bad String")
