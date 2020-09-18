#!/bin/python3

# https://www.hackerrank.com/challenges/kangaroo/problem

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if v1 < v2:
        return 'NO'
    
    if x1 < x2 and v1 > v2:
        del_pos = abs(x1 - x2)
        del_vel = abs(v1 - v2)

        if (del_pos % del_vel) == 0:
            return 'YES'

    return 'NO'
    

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
