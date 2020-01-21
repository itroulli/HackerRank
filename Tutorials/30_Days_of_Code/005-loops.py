# Name: Day 5: Loops
# Problem: https://www.hackerrank.com/challenges/30-loops/problem
# Score: 30


n = int(input())
for multi in range(1, 11):
    print(str(n) + ' x ' + str(multi) + ' = ' + str(n * multi))
