#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
maxi = None
for i in range(4):
    for j in range(4):
        current = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
                  arr[i+1][j+1] + \
                  arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if maxi == None or current > maxi:
            maxi = current
print(maxi)

'''
 i,j    i, j+1    i, j+2
i+1,j   i+1, j+1  i+1, j+2
i+2,j   i+2, j+1  i+2, j+2
'''
#[[0, 2, 1, 3, 4, 5], [3, 1, 2, 3, 4, 1], [7, 8, 6, 4, 9, 0], [3, 5, 6, 7, 1, 9], [4, 5, 7, 1, 9, 7], [2, 3, 4, 1, 6, 7]]
