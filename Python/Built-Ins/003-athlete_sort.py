# Name: Athlete Sort
# Problem: https://www.hackerrank.com/challenges/python-sort-sort/problem
# Score: 30

# Following HackerRank's template:

#!/bin/python3


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr.sort(key= lambda x: x[k])
    for athlete in arr:
        print(*athlete)

# OR, this suggestion in discussion:

# N, M = map(int, input().split())
# rows = [input() for _ in range(N)]
# K = int(input())
#
# for row in sorted(rows, key=lambda row: int(row.split()[K])):
#     print(row)
