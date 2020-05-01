from itertools import groupby

dataset = groupby(input())
for index, item in dataset:
    print(f'({len(list(item))}, {index} )', end=' ')


# pointer = -1
# count = 0
# for i in range(len(dataset)):
#     x = int(dataset[i])
#     if x != pointer and pointer != -1:
#         print(f'({count}, {pointer})', end=' ')

#     if x == pointer:
#         count += 1
#     else:
#         count = 1
#         pointer = x
# print(f'({count}, {pointer})')