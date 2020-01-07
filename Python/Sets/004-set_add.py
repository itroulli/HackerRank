# Name: Set .add()
# Problem: https://www.hackerrank.com/challenges/py-set-add/problem
# Score: 10


# Enter your code here. Read input from STDIN. Print output to STDOUT
s = set()
n = int(input())
for _ in range(n):
    s.add(input())
print(len(s))
