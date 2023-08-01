import re

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        print(re.match(r"^[+\-]?\d*\.\d+$", input()) is not None)
