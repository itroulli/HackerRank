# Name: Zeros and Ones
# Problem: https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
# Score: 20


import numpy

shape = tuple(map(int, input().split()))
print(numpy.zeros(shape, dtype = numpy.int))
print(numpy.ones(shape, dtype = numpy.int))
