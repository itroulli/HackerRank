# Name: Word Order
# Problem: https://www.hackerrank.com/challenges/word-order/problem
# Score: 50


from collections import Counter

cnt = Counter()
n = int(input())
for _ in range(n):
    cnt[input()] += 1
print(len(cnt))
print(*cnt.values())
