# Name: Re.split()
# Problem: https://www.hackerrank.com/challenges/re-split/problem
# Score: 20


import re

regex_pattern = r"[.,]"	# Do not delete 'r'.

print("\n".join(re.split(regex_pattern, input())))
