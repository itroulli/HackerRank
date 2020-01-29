# Name: Concatenate
# Problem: https://www.hackerrank.com/challenges/np-concatenate/problem
# Score: 20


import numpy

n, m,  _ = list(map(int, input().split()))

print(numpy.concatenate((numpy.array([input().split() for _ in range(n)], dtype=int),
                         numpy.array([input().split() for _ in range(m)], dtype=int)), axis=0))

# OR, more readable:

# arr1 = numpy.array([input().split() for _ in range(n)], dtype = int)
# arr2 = numpy.array([input().split() for _ in range(m)], dtype = int)
# print(numpy.concatenate((arr1, arr2), axis=0))
