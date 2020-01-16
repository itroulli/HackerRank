# Name: Zipped!
# Problem: https://www.hackerrank.com/challenges/zipped/problem
# Score: 10

# Enter your code here. Read input from STDIN. Print output to STDOUT
_, m = list(map(int, input().split()))
subjects =[]
for _ in range(m):
    subjects.append(list(map(float, input().split())))
for student in zip(*subjects):
    print(f"{sum(student)/m:.1f}")
