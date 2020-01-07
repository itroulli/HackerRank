# Name: Check Strict Superset
# Problem: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Score: 10

# Initial thought
# A = set(input().split())
# result = []
# for _ in range(int(input())):
#     B = input().split()
#     if A.issuperset(B) and not A.issubset(B):
#         result.append(True)
#     else:
#         result.append(False)
# print(sum(result) == len(result))

# After reading about all() and '>' set operator
# https://www.w3schools.com/python/ref_func_all.asp
# https://docs.python.org/3.6/library/stdtypes.html#set-types-set-frozenset
A = set(input().split())
result = []
for _ in range(int(input())):
    result.append(A > set(input().split()))
print(all(result))

