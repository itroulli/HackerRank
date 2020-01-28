# Name: Shape and Reshape
# Problem: https://www.hackerrank.com/challenges/np-shape-reshape/problem
# Score: 20

import numpy

arr = numpy.array(input().split(), int)
print(numpy.reshape(arr, (3, 3)))
