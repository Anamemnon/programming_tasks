if __name__ == '__main__':
    size = int(input())
    arr = [i for i in input().split()]

    from collections import Counter
    c = Counter(arr)

    print(c.most_common()[-1][0])

