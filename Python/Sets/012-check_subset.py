# Name: Check Subset
# Problem: https://www.hackerrank.com/challenges/py-check-subset/problem
# Score: 10


for _ in range(int(input())):
    _, A = input(), set(input().split())
    _, B = input(), set(input().split())
    print(A.intersection(B) == A)
    # alternatively:
    # print(A.issubset(B))
