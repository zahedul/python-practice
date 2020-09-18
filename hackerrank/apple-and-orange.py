#!/bin/python3

#https://www.hackerrank.com/challenges/apple-and-orange/problem

import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Complete this function
    a_point = 0
    b_point = 0
    for data in apples:
        if (a + data) >= s and (a + data) <= t:
            a_point += 1

    for data in oranges:
        if (b + data) >= s and (b + data) <= t:
            b_point += 1
    
    print(a_point)
    print(b_point)
    

if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    countApplesAndOranges(s, t, a, b, apple, orange)
