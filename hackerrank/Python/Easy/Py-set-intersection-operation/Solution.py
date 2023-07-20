# py-set-intersection-operation
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true

if __name__ == '__main__':
    input()
    students_set1 = set(s for s in input().split())
    input()
    students_set2 = set(s for s in input().split())

    print(len(students_set1.intersection(students_set2)))