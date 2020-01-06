# Name: Find the Runner-Up Score!
# Problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Score: 10


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique = sorted(set(arr))

    print(unique[-2])
