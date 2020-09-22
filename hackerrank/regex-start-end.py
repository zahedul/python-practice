import re

S = input()
k = input()

m = re.search(k, S)
pattern = re.compile(k)
if not m:
    print("(-1, -1)")
    
while m:
    print(f'({m.start()}, {m.end()-1})')
    m = pattern.search(S, m.start()+1)