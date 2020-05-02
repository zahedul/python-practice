import re

t = int(input())
for _ in range(t):
    regex_pattern = input()

    try:
        re.compile(regex_pattern)
    except Exception as e:
        print('False')
    else:
        print('True')