from collections import Counter

x = input()
sizes = Counter(v for v in input().split())
n = int(input())
total_price = 0


for _ in range(n):
    size, cost = input().split()

    if size in sizes.keys() and sizes[size] > 0:
        total_price += int(cost)
        sizes[size] -= 1

print(total_price)
