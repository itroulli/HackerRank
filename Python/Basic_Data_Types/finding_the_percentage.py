# Name: Finding the percentage
# Problem: https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Score: 10


import statistics

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(f"{statistics.mean(student_marks[query_name]):.2f}")
