# Name: Set .union() Operation
# Problem: https://www.hackerrank.com/challenges/py-set-union/problem
# Score: 10


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng = set(input().split())
b = int(input())
fr = set(input().split())
print(len(eng.union(fr)))
