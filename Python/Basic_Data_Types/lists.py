if __name__ == '__main__':
    n = int(input())
    method_map = {'insert': list.insert,
                  'print': print,
                  'remove': list.remove,
                  'append': list.append,
                  'sort': list.sort,
                  'pop': list.pop,
                  'reverse': list.reverse}
    listA = []
    for _ in range(n):
        method, *args = input().split(' ')
        method_map[method](listA, *map(int, args))
