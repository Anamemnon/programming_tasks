T = int(input())

for _ in range(T):
    a, b = input().split()

    try:
        print(int(a) // int(b))
    except ValueError as e:
        print("Error Code:", e)
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
