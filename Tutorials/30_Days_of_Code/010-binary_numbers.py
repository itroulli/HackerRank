# Name: Day 10: Binary Numbers
# Problem: https://www.hackerrank.com/challenges/30-binary-numbers/problem
# Score: 30


if __name__ == '__main__':
    n = int(input())
    print(max(map(len, bin(n).replace('0b', '').split('0'))))
