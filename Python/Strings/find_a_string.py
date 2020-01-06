# Name: Find a string
# Problem: https://www.hackerrank.com/challenges/find-a-string/problem
# Score: 10


def count_substring(string, sub_string):
    sub_l = len(sub_string)
    count = 0
    for index in range(len(string)-sub_l+1):
        if string[index:index+sub_l] == sub_string:
            count += 1
    return count
