# Name: itertools.product()
# Problem: https://www.hackerrank.com/challenges/itertools-product/problem
# Score: 10


from itertools import product

a_set = list(map(int, input().split()))
b_set = list(map(int, input().split()))

print(*list(product(a_set, b_set)))
