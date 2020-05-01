for _ in range(int(input())):
    _ = input()
    set_a = set(map(int, input().split()))

    _ = input()
    set_b = set(map(int, input().split()))

    print(set_a.issubset(set_b))