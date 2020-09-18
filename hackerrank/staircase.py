#!/bin/python3

#https://www.hackerrank.com/challenges/staircase/problem

import sys

def staircase(n):
    # Complete this function
    for x in range(1, n):
        for i in range(0, (n-x)):
            #print("i=%s", i)
            print(" ",end='', flush=True)
        for j in range(0, x):
            print("#", end='', flush=True)
        print("")
    for k in range(0, n):
        print("#", end='', flush=True)
    print("")
    

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
