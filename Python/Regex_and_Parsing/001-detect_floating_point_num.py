# Name: Detect Floating Point Number
# Problem: https://www.hackerrank.com/challenges/introduction-to-regex/problem
# Score: 20


import re


for _ in range(int(input())):
    print(bool(re.match(r'^[-+]?\d*\.\d+$', input())))
