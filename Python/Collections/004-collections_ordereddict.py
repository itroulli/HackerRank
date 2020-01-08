# Name: Collections.OrderedDict()
# Problem: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# Score: 20


from collections import OrderedDict

ord = OrderedDict()

n = int(input())
for _ in range(n):
    key, value = input().rsplit(" ", 1)
    ord[key] = ord.get(key, 0) + int(value)
for item in ord.items():
    print(item[0], item[1])
