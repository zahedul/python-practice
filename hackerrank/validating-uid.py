import re
x = re.compile(r'(?!.*(.).*\1)(?=.*\d.*\d.*\d)(?=.*[A-Z].*[A-Z])[A-Za-z0-9]{10}')

t = int(input())

for _ in range(t):
    uid = input()
    print('Valid' if x.match(uid) else 'Invalid')
