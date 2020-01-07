# Name Symmetric Difference
# Problem: https://www.hackerrank.com/challenges/symmetric-difference/problem
# Score: 10


_, set_a, _, set_b = (int(input()), set(map(int, input().split())), int(input()), set(map(int, input().split())))
for x in sorted(set_a.symmetric_difference(set_b)):
    print(x)
