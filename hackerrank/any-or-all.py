_ = int(input())

data = list(map(int, input().split()))

print(all(i >=0 for i in data) and any(str(i)==str(i)[::-1] for i in data))