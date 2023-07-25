_ = input()

main_set = set(int(v) for v in input().split())

n = int(input())

for _ in range(n):
    operation = input().split()[0]
    temp_set = set(int(v) for v in input().split())
    eval(f'main_set.{operation}({temp_set})')

print(sum(main_set))
