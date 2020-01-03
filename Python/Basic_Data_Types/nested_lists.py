if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        scores.append(score)
    unique_s = list(set(scores))
    unique_s.sort()
    s_lowest = [student[0] for student in students if student[1] == unique_s[1]]
    s_lowest.sort()
    print(*s_lowest, sep="\n")
