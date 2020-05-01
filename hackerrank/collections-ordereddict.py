from collections import OrderedDict

n = int(input())
item_list = OrderedDict()

for i in range(n):
    name, space, price = input().rpartition(" ")
    item_list[name] = item_list.get(name, 0) + int(price)

for name in item_list:
    print(f'{name} {item_list[name]}')