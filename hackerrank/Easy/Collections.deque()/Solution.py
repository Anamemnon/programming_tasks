# collections.deque()
# https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true


if __name__ == '__main__':
    from collections import deque
    n = int(input())
    d = deque()

    for _ in range(n):
        line = input().split()
        if len(line) == 1:
            exec(f'd.{line[0]}()')
        elif len(line) == 2:
            exec(f'd.{line[0]}({line[-1]})')

    print(*d)
