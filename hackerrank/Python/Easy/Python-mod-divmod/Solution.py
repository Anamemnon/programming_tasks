# python-mod-divmod
# https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=true

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    result = divmod(a, b)

    print(result[0])
    print(result[1])
    print(result)