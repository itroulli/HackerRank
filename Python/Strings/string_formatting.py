def print_formatted(number):

    width = len(bin(number)[2:])
    for num in range(1, number+1):
        print(str(num).rjust(width), str(oct(num))[2:].rjust(width),
              str(hex(num))[2:].upper().rjust(width), str(bin(num)[2:].rjust(width)), sep=" ")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
