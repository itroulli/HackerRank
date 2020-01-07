# Name: Polar Coordinates
# Problem: https://www.hackerrank.com/challenges/polar-coordinates/problem
# Score: 10


import cmath

num = complex(input())
print(f"{abs(num):.3f}")
print(f"{cmath.phase(num):.3f}")
