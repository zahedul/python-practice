#!/bin/python3

#https://www.hackerrank.com/challenges/mini-max-sum/problem

import sys

def miniMaxSum(arr):
    # Complete this function
    arr.sort()
    arr_sum = sum(arr)
    min_sum = arr_sum - arr[len(arr) - 1]
    max_sum = arr_sum - arr[0]
    print("%s %s" % (min_sum, max_sum))

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
