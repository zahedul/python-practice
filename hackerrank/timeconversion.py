#!/bin/python3

#https://www.hackerrank.com/challenges/time-conversion/problem

import sys

def timeConversion(s):
    # Complete this function
    if "PM" in s:
        data = s.replace("PM", "")
        hour, minute, second = data.split(":")
        if int(hour) < 12:
            hour = int(hour) + 12
        return "%s:%s:%s" % (hour, minute, second)
    else:
        data = s.replace("AM", "")
        hour, minute, second = data.split(":")
        if int(hour) == 12:
            hour = '00'

        return "%s:%s:%s" % (hour, minute, second)

if __name__ == "__main__":
    s = input().strip()
    result = timeConversion(s)
    print(result)
