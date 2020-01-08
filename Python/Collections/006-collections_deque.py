# Name: Collections.deque()
# Problem: https://www.hackerrank.com/challenges/py-collections-deque/problem
# Score: 20


from collections import deque

d = deque()
for _ in range(int(input())):
    method, *args = input().split()
    getattr(d, method)(*map(int,args))
print(*d)
