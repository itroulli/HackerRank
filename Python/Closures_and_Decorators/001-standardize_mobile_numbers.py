# Name: Standardize Mobile Number Using Decorators
# Problem: https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
# Score: 30


# 1st try:
def wrapper(f):
    def fun(l):
        for i, num in enumerate(l):
            l[i] = '+91 ' + num[-10:-5] + ' ' + num[-5:]
        ret = f(l)
        return ret
    return fun

# 2nd try, using list comprehension:
# def wrapper(f):
#     def fun(l):
#             f(['+91 ' + num[-10:-5] + ' ' + num[-5:] for num in l])
#     return fun

# 3rd try, using f-string:
# def wrapper(f):
#     def fun(l):
#             f([f'+91 {num[-10:-5]} {num[-5:]}' for num in l])
#     return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
