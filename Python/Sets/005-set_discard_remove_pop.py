# Name: Set .discard(), .remove() & .pop()
# Problem:
# Score: 10
# Difficulty: Easy


n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    method, *args = input().split()
    getattr(s, method)(*map(int,args))
print(sum(s))

# OR
# methods = {
#    'pop' : s.pop,
#    'remove' : s.remove,
#    'discard' : s.discard
# }
# for _ in range(N):
#     method, *args = input().split()
#     methods[method](*map(int,args))
