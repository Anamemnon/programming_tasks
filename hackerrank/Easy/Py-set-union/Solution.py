# py-set-union
# https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true

if __name__ == '__main__':
    input()
    students_set1 = set(s for s in input().split())
    input()
    students_set2 = set(s for s in input().split())

    print(len(students_set1.union(students_set2)))
