# https://www.hackerrank.com/challenges/between-two-sets/problem
N = int(input())

# Get the array 
numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))

sumArray = []

# Write the logic here:
for i in range(0, N):
    sum_data = numArray1[i] + numArray2[i]
    sumArray.append(sum_data)


# Print the sumArray
for element in sumArray:
    print(element, end=" ")
    
print("")
