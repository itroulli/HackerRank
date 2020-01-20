# Name: Day 1: Data Types
# Problem: https://www.hackerrank.com/challenges/30-data-types/problem
# Score: 30

i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
i2, d2, s2 = int(input()), float(input()), input()
# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.
print(i+i2)
# Print the sum of the double variables on a new line.
print(f"{d+d2:.1f}")
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s+s2)
