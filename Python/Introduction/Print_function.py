# Name: Print Function
# Problem: https://www.hackerrank.com/challenges/python-print/problem
# Score: 20

if __name__ == '__main__':
    n = int(input())
    print(*range(1, n+1), sep="")
