# Name: Collections.namedtuple()
# Problem: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# Score: 20


from collections import namedtuple

n = int(input())
Student = namedtuple('Student', input().split())
total = 0
for _ in range(n):
    stu = Student(*input().split())
    total += int(stu.MARKS)
print(f"{total/n:.2f}")
