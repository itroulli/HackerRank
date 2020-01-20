# Name: Day 3: Intro to conditional statements
# Problem: https://www.hackerrank.com/challenges/30-conditional-statements/problem
# Score: 30


if __name__ == '__main__':
    n = int(input())
    if n%2 == 0 and (n>20 or 2 <= n <= 6):
        print("Not Weird")
    else:
        print("Weird")
