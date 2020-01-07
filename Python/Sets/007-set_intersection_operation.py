# NameL Set .intersection() Operation
# Problem: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
# Score: 10


_, eng, _, fr = [int(input()), set(map(int,input().split())), int(input()), set(map(int, input().split()))]
print(len(eng.intersection(fr)))
