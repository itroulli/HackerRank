# Name: Day 8: Dictionaries and Maps
# Problem: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# Score: 30


# Enter your code here. Read input from STDIN. Print output to STDOUT
phonebook = {}
for _ in range(int(input())):
    entry = input().split()
    phonebook[entry[0]] = entry[1]
while True:
    try:
        name = input()
        if name in phonebook:
            print(f"{name}={phonebook[name]}")
        else:
            print("Not found")
    except EOFError:
        break
