# Name: Triangle Quest 2
# Problem: https://www.hackerrank.com/challenges/triangle-quest-2/problem
# Score: 20


for i in range(1, int(input())+1):
    print(pow(((pow(10, i)-1)//9), 2))
