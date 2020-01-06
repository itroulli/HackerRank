# Name: Tuples
# Problem: https://www.hackerrank.com/challenges/python-tuples/problem
# Score: 10


if __name__ == '__main__':
    n, integer_list = (int(input()), tuple(map(int, input().split())))
    print(hash(integer_list))
