# Name: Day 14: Scope
# Problem: https://www.hackerrank.com/challenges/30-scope/problem
# Score: 30


class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        self.maximumDifference = max(a) - min(a)

# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

# For a faster implementation we could write a loop that finds max and min of the list
# in the same pass instead of passing through twice with the built-in functions.
