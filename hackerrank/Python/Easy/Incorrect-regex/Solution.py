# incorrect-regex
# Pypy3
# https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true

if __name__ == '__main__':
    import re

    for _ in range(int(input())):
        try:
            re.compile(input())
            print("True")
        except re.error:
            print("False")

