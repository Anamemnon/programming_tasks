if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        input()
        main_set = set(i for i in input().split())
        input()
        subset = set(i for i in input().split())
        print(main_set.issubset(subset))