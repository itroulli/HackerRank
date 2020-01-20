# Name: Any or All
# Problem: https://www.hackerrank.com/challenges/any-or-all/problem
# Score: 20

# Enter your code here. Read input from STDIN. Print output to STDOUT
_, elements = input(), input().split()
print(all([int(elem)>0 for elem in elements]) and any([elem == elem[::-1] for elem in elements]))
