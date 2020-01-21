# Name: Map and Lambda Function
# Problem: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
# Score: 20

cube = lambda x: x**3  # complete the lambda function


def fibonacci(n):
    fib = [0, 1]
    if n <= 2:
        return fib[:n]
    else:
        for i in range(n-2):
            fib.append(fib[i] + fib[i+1])
        return fib
    # return a list of fibonacci numbers


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
