# Name: Day 7: Arrays
# Problem: https://www.hackerrank.com/challenges/30-arrays/problem
# Score: 30


if __name__ == '__main__':
    _ = input()

    arr = list(map(int, input().rstrip().split()))
    print(*reversed(arr))
