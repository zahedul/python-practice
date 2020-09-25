import re

regex = r'[789]\d{9}$'

[print('YES' if re.match(regex, input()) else 'NO') for _ in range(int(input()))]