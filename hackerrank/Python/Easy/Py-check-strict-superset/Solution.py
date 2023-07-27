if __name__ == '__main__':
    set_a = set(s for s in input().split())

    n = int(input())
    superset = True

    for _ in range(n):
        temp_set = set(s for s in input().split())
        superset = set_a.issuperset(temp_set)
        if not superset:
            break

    print(superset)
