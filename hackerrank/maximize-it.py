k, m = list(map(int, input().split()))

result = 0
for _ in range(k):
    data_set = list(map(int, input().split()))
    i = max(data_set)
    result += (i**2)

print(result)