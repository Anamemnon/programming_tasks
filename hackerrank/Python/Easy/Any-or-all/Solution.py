if __name__ == '__main__':
    input()
    arr = [int(i) for i in input().split()]
    isAllPositive = all(i > 0 for i in arr)
    isAnyPolindrom = any(str(i) == str(i)[::-1] for i in arr)

    print(isAnyPolindrom and isAllPositive)