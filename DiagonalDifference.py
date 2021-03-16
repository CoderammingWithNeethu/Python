#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    ln = len(arr)
    l1 = [i for i in range(ln)]
    l2 = [i for i in range(ln-1,-1,-1)]
    left_cor = []
    right_cor = []
    for i in zip(l1,l1):
        left_cor.append(i)
        
    for i in zip(l1,l2):
        right_cor.append(i)
    
    left_val = [arr[i[0]][i[1]] for i in left_cor]
    right_val = [arr[i[0]][i[1]] for i in right_cor]
                
    print(abs(sum(left_val)-sum(right_val)))
    
    #0,0 1,1 2,2
    #0,2 1,1 2,0            

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    diagonalDifference(arr)


'''
Solution 1 : 
n = int(input())
mat = []
for _ in range(n):
    row = [int(i) for i in input().split()]
    mat.append(row)

s1 = 0
s2 = 0
for i in range(n):
    s1 += mat[i][i]
    s2 += mat[i][n-1-i]
print(abs(s1-s2))


Solution 2 :
N = int(input())
diff = 0
a, b = 0, N - 1
for i in range(N):
    numbers = list(map(int, input().split()))
    diff += numbers[b] - numbers[a]
    a += 1
    b -= 1
print(abs(diff))

Solution 3 :
N = int(input())
nMinsOne = N - 1
sumDiag1 = 0
sumDiag2 = 0

for i in range(N):
    line = input().split()
    sumDiag1 += int(line[i])
    sumDiag2 += int(line[nMinsOne - i])

print (abs(sumDiag1 - sumDiag2))
    
OR 

size=int(input())
thematrix=[]
firstdiag=[]
seconddiag=[]
for i in range(size):
    line = input().strip().split(' ')
    line=[int(j) for j in line]
    thematrix.append(line)
for i in range(size):
    firstdiag.append(thematrix[i][i])
    seconddiag.append(thematrix[i][(size-1)-i])
print(abs(sum(firstdiag)-sum(seconddiag))) 

Solution :

def diag_diff(matrix, size):
    sum_first_diag = 0
    sum_second_diag = 0
    for i in range(size):
        for j in range(size):
            if i == j:
                sum_first_diag += int(matrix[i][j])
                sum_second_diag += int(matrix[i][-(j+1)])

'''