# Name: Piling Up!
# Problem: https://www.hackerrank.com/challenges/piling-up/problem
# Score: 50


from collections import deque


for _ in range(int(input())):
    _, d = int(input()), deque(map(int, input().split()))

    for length in reversed(sorted(d)):
        if d[0] == length:
            d.popleft()
        elif d[-1] == length:
            d.pop()
        else:
            print("No")
            break
    else:
        print("Yes")
