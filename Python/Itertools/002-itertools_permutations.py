# Name: itertools.permutations()
# Problem: https://www.hackerrank.com/challenges/itertools-permutations/problem
# Score: 10


from itertools import permutations

s, k = input().split()

ls = sorted(["".join(x) for x in list(permutations(s, int(k)))])
print(*ls, sep="\n")

