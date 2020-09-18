#!/bin/python3

#https://www.hackerrank.com/challenges/plus-minus/problem
import sys

def plusMinus(arr):
    # Complete this function
    count_pos = 0
    count_zero = 0
    count_neg = 0
    for data in arr:
        if data == 0:
            count_zero += 1
        if data < 0:
            count_neg += 1
        if data > 0:
            count_pos += 1
    
    print(format(count_pos/len(arr), '.6f'))
    print(format(count_neg/len(arr), '.6f'))
    print(format(count_zero/len(arr), '.6f'))
    
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
