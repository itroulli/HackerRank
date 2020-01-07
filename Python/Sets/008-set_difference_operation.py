# Name: Set .difference() Operation
# Problem: https://www.hackerrank.com/challenges/py-set-difference-operation/problem
# Score: 10


_, eng, _, fr = [int(input()), set(map(int, input().split())), int(input()), set(map(int, input().split()))]
print(len(eng.difference(fr)))
