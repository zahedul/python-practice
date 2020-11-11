import math

ab = int(input())
bc = int(input())

res = math.atan2(ab,bc)

print(int(math.degrees(res)), chr(176), sep='')