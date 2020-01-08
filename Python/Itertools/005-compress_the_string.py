# Name: Compress the String!
# Problem: https://www.hackerrank.com/challenges/compress-the-string/problem
# Score: 20


from itertools import groupby

s = input()

print(*[(len(list(g)), int(k)) for k, g in groupby(s)], sep=" ")
