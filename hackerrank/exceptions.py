t = int(input())

for _ in range(t):
    a, b = input().split()

    try:
        print(int(int(a)/int(b)))
    except ZeroDivisionError as e:
        print('Error Code: integer division or modulo by zero')
    except Exception as e:
        print(f'Error Code: {e}')