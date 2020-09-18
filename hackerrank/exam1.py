#!/bin/python3

import sys
import os

def howManyAgentsToAdd(noOfCurrentAgents, callsTimes):
    data = sum(callsTimes, [])

    count = 0
    for i in range(1, len(data)):
        if (data[i] < data[i-1]):
            count += 1
    if count == 0:
        return 0
    return count - noOfCurrentAgents


if __name__ == "__main__":
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    noOfCurrentAgents = int(input())

    callsTimes_rows = 0
    callsTimes_cols = 0
    callsTimes_rows = int(input())
    callsTimes_cols = int(input())

    callsTimes = []
    for callsTimes_i in range(callsTimes_rows):
        callsTimes_temp = [int(callsTimes_t) for callsTimes_t in input().strip().split(' ')]
        callsTimes.append(callsTimes_temp)

    res = howManyAgentsToAdd(noOfCurrentAgents, callsTimes);
    print(res)
    # f.write(str(res) + "\n")


    # f.close()