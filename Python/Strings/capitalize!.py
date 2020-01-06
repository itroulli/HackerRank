# Name: Capitalize!
# Problem:  https://www.hackerrank.com/challenges/capitalize/problem
# Score: 20


import os


def solve(s):
    return " ".join(map(str.capitalize, s.split(" ")))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')
    fptr.close()
