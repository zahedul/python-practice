#!/bin/python3

# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    max_num = max(ar)

    return ar.count(max_num)

if __name__ == "__main__":
    n = int(input().strip())
    ar = list(map(int, input().strip().split(' ')))
    result = birthdayCakeCandles(n, ar)
    print(result)