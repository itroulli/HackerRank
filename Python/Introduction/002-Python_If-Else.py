# Name: Python If-Else
# Problem: https://www.hackerrank.com/challenges/py-if-else/problem
# Score: 10

if __name__ == '__main__':
    n = int(input())
    if (n % 2 == 1) or (6 <= n <= 20):
        print("Weird")
    elif (2 <= n <= 5) or (n > 20):
        print("Not Weird")
