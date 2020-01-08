# Name: Company Logo
# Problem: https://www.hackerrank.com/challenges/most-commons/problem
# Score: 30


from collections import Counter


if __name__ == '__main__':
    for each in Counter(sorted(input())).most_common(3): print(*each)
