# Name: Set .symmetric_difference() Operation
# Problem: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
# Score: 10


_, eng, _, fr = (int(input()), set(map(int, input().split())), int(input()), set(map(int, input().split())))
print(len(eng.symmetric_difference(fr)))
