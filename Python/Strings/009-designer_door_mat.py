# Name: Designer Door Mat
# Problem: https://www.hackerrank.com/challenges/designer-door-mat/problem
# Score: 10


n, m = map(int, input().split(" "))
symbol = ".|."
for row in range(n//2):
    print((row*symbol).rjust((m-3)//2, "-") + symbol + (row*symbol).ljust((m-3)//2, "-"))
print("WELCOME".center(m, "-"))
for row in range(n//2-1, -1, -1):
    print((row*symbol).rjust((m-3)//2, "-") + symbol + (row*symbol).ljust((m-3)//2, "-"))
