import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    reversed_arr = arr[::-1]

    return numpy.array(reversed_arr, float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)