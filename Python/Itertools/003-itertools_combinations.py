# Name: itertools.combinations()
# Problem: https://www.hackerrank.com/challenges/itertools-combinations/problem
# Score: 10


from itertools import combinations

s, k = input().split()

for comb in range(1, int(k)+1):
    print(*["".join(x) for x in list(combinations(sorted(s), comb))], sep="\n")
