# Name: Incorrect Regex
# Problem: https://www.hackerrank.com/challenges/incorrect-regex/problem
# Score: 20


import re

for _ in range(int(input())):
    try:
        reg = re.compile(input())
        print(True)
    except re.error:
        print(False)

# Details on how to make this check more effective:
# https://stackoverflow.com/questions/19630994/how-to-check-is-a-string-is-a-valid-regex-python#comment29145368_19630994