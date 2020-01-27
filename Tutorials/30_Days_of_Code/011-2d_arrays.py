# Name: Day 11: 2D Arrays
# Problem: https://www.hackerrank.com/challenges/30-2d-arrays/problem
# Score: 30


def array2D(arr):
    sums = []
    for i in range(4):
        for j in range(4):
            hsum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + \
                   arr[i + 2][j + 2]
            sums.append(hsum)
    return max(sums)


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(array2D(arr))
