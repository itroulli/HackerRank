def print_rangoli(size):
    # your code goes here
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    carpet = []
    for idx in range(size):
        temp = "-".join(abc[idx:size])
        carpet.append((temp[::-1] + temp[1:]).center(4*size - 3, "-"))
    print("\n".join(carpet[:0:-1]+carpet))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
