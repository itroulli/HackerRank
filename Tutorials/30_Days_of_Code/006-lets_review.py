# Name: Day 5: Let's Review
# Problem: https://www.hackerrank.com/challenges/30-review-loop/problem
# Score: 30

# Enter your code here. Read input from STDIN. Print output to STDOUT
words = [input() for _ in range(int(input()))]
for word in words:
    odd, even = '', ''
    for num, letter in enumerate(word):
        if num%2 == 0:
            even += letter
        else:
            odd += letter
    print(even + ' ' + odd)

# Significantly simpler:
#
# for _ in range(int(input())):
#     word = input()
#     print(word[::2], word[1::2])
