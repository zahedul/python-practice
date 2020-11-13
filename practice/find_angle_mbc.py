import math

ab = int(input())
bc = int(input())

res = math.atan2(ab,bc)

print(int(round(math.degrees(res))), chr(176), sep='')