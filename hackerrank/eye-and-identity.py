import numpy

m, n = map(int, input().split(' '))

numpy.set_printoptions(sign=' ')
print(numpy.eye(m, n, k = 0))