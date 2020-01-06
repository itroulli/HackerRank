# Name: Text Wrap
# Problem: https://www.hackerrank.com/challenges/text-wrap/problem
# Score: 10


import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
