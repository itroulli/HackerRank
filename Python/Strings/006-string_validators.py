# Name: String Validators
# Problem: https://www.hackerrank.com/challenges/string-validators/problem
# Score: 10


if __name__ == '__main__':
    s = input()
    st = set(s)
    anum = False
    alpha = False
    dig = False
    low = False
    upper = False
    for letter in st:
        if not anum:
            anum = letter.isalnum()
        if not alpha:
            alpha = letter.isalpha()
        if not dig:
            dig = letter.isdigit()
        if not low:
            low = letter.islower()
        if not upper:
            upper = letter.isupper()

    print(f"{anum}\n{alpha}\n{dig}\n{low}\n{upper}")

