if __name__ == '__main__':
    students, marks = [int(i) for i in input().split()]
    matrix = [[float(mark) for mark in input().split()] for _ in range(marks)]

    for j in range(students):
        sum_ = 0
        for i in range(marks):
            sum_ += matrix[i][j]
        print(round(sum_ / marks, 1))

