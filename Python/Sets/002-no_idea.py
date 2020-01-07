# Name: No Idea!
# Problem: https://www.hackerrank.com/challenges/no-idea/problem
# Score: 50
# Difficulty: Medium


# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
arr = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
happiness = 0
for x in arr:
    if x in set_a:
        happiness += 1
    elif x in set_b:
        happiness -= 1
print(happiness)
