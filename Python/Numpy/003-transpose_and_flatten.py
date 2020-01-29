# Name: Transpose and Flatten
# Problem: https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
# Score: 20


import numpy

arr = numpy.array([list(map(int,input().split())) for _ in range(int(input().split()[0]))])
print(numpy.transpose(arr))
print(arr.flatten())