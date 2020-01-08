# Name: collections.Counter()
# Problem: https://www.hackerrank.com/challenges/collections-counter/problem
# Score: 10


from collections import Counter

_, shoe_size, N = input(), input().split(), int(input())

count = Counter(shoe_size)
earned = 0
for cust in range(N):
    size, money = input().split()
    if (size in count) and (count[size] > 0):
        earned += int(money)
        count[size] -= 1
print(earned)
