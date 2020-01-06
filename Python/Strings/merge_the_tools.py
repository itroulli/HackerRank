# Name: Merge the Tools!
# Problem: https://www.hackerrank.com/challenges/merge-the-tools/problem
# Score: 40


def merge_the_tools(string, k):
    t = []
    u = []
    s = set()
    n = len(string)
    for i in range(n // k):
        t.append(string[i * k:(i + 1) * k])
        for c in t[i]:
            if c not in s:
                s.add(c)
                u.append(c)
        print(''.join(u))
        u = []
        s = set()


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
