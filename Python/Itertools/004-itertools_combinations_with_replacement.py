# Name: itertools.combinations_with_replacement
# Problem: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
# Score: 10


from itertools import combinations_with_replacement

s, k = input().split(" ")

ls = ["".join(x) for x in list(combinations_with_replacement(sorted(s), int(k)))]
print(*ls, sep="\n")
