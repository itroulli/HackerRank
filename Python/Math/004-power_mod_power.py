# Name: Power - Mod Power
# Problem: https://www.hackerrank.com/challenges/python-power-mod-power/problem
# Score: 10


# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b, m = [int(input()) for _ in range(3)]
print(pow(a, b))
print(pow(a, b, m))
