# Name: Set Mutations
# Problem: https://www.hackerrank.com/challenges/py-set-mutations/problem
# Score: 10


_, mainset = input(), set(input().split())
for _ in range(int(input())):
    method, _ = input().split()
    tempset = input().split()
    getattr(mainset, method)(tempset)
mainset = set(map(int, mainset))
print(sum(mainset))
