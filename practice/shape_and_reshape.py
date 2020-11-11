import numpy

def shapes(arr):
    # complete this function
    # use numpy.array

    return numpy.reshape(numpy.array(arr, int), (3,3))

arr = input().strip().split(' ')
result = shapes(arr)
print(result)