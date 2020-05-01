super_set = set(map(int, input().split()))

n = int(input())

is_super_set = True

for _ in range(n):
    set_i = set(map(int, input().split()))

    if is_super_set == False:
        continue
    if len(set_i) >= len(super_set):
        is_super_set = False
    elif set_i.issubset(super_set) !=True:
        is_super_set = False

print(is_super_set)