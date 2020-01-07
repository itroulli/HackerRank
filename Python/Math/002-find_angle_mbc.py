# Name: Find Angle MBC
# Problem: https://www.hackerrank.com/challenges/find-angle/problem
# Score: 10


import math

AB = int(input())
BC = int(input())

tanx = AB/BC
# from https://stackoverflow.com/a/3216630/7903159
degree_sign= u'\N{DEGREE SIGN}'  # could also be chr(176)
print(str(round(math.degrees(math.atan(tanx)))) + degree_sign)
