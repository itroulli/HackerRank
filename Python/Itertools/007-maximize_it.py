# Name: Maximize it!
# Problem: https://www.hackerrank.com/challenges/maximize-it/problem
# Score: 50


from itertools import product

n, m = list(map(int, input().split()))
inputs = (list(map(int, input().split()))[1:] for _ in range(n))
modulos = map(lambda x: sum(item**2 for item in x)%m, product(*inputs))
print(max(modulos))
