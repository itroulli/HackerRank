# Name: Day 2: Operators
# Problem: https://www.hackerrank.com/challenges/30-operators/problem
# Score: 30


def solve(meal_cost, tip_percent, tax_percent):
    print(round(meal_cost * ((100 + tip_percent)/100) + (meal_cost * (tax_percent/100))))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
