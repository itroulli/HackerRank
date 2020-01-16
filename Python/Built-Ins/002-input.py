# Name: Input()
# Problem: https://www.hackerrank.com/challenges/input/problem
# Score: 20

# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = map(int, input().split())
print(k == eval(input()))
