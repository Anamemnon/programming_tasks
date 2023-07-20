# Set .discard(), .remove() & .pop()
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

if __name__ == '__main__':
    n = int(input())

    set_ = set(int(i) for i in input().split())

    N = int(input())

    for _ in range(N):
        line = input().split()
        if len(line) == 1:
            exec(f'set_.{line[0]}()')
        elif len(line) == 2:
            exec(f'set_.{line[0]}({line[-1]})')
    print(sum(set_))
