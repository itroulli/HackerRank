# Name: Iterables and Iterators
# Problem: https://www.hackerrank.com/challenges/iterables-and-iterators/problem
# Score: 40


from itertools import combinations

_, letters, k = input(), input().split(), input()

comb = list(combinations(letters, int(k)))
not_a = filter(lambda x: 'a' in x, comb)
print(f"{len(list(not_a))/len(comb):.3f}")
