from collections import OrderedDict

n = int(input())
item_list = OrderedDict()

for i in range(n):
    name = input()
    item_list[name] = item_list.get(name, 0) + 1

print(len(item_list))
for name in item_list:
    print(f'{item_list[name]}', end= ' ')
print()