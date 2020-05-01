from itertools import combinations 

_ = input()

data_set = input().split()
r = int(input())

combination_data = list(combinations(data_set, r))
total_len = len(combination_data)

count = 0
for item in combination_data:
    if 'a' in item:
        count += 1

print('{:.4f}'.format(count/total_len))