# Name: DefaultDict Tutorial
# Problem: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# Score: 20


from collections import defaultdict

d = defaultdict(list)
n, m = map(int, input().split())

for i in range(1, n+1):
    d[input()].append(i)

for _ in range(m):
    b = input()
    if b in d:
        print(*d[b])
    else:
        print(-1)
