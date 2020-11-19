# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:33:31 2020

@author: nnath
"""

'''
PROBLEM STATEMENT :
Given an integer, n, print the following values for each integer i from 1 to n:

Decimal
Octal
Hexadecimal (capitalized)
Binary

The four values must be printed on a single line in the order specified above for each i from 1 to n. 
Each value should be space-padded to match the width of the binary value of n.

'''

n = int(input())

#replace function
#w = len(bin(n).replace('0b',''))

w = len(bin(n)[2:])

for i in range(1,n+1):
    #Solution 1 with inbuilt functions for conversion
    #print(i,'\t',oct(i)[2:],'\t',hex(i)[2:].upper(),'\t',bin(i)[2:])
    
    #Solution 2 with string formatting 
    #print(i,'\t{:0o}'.format(i),'\t{:0x}'.format(i).upper(),'\t{:0b}'.format(i))
    
    #Space-padding - str.rjust(width[, fillchar])   --returns the string right justified in a string of length width 
    #print(str(i).rjust(2),'{:0o}'.format(i).rjust(2),'{:0x}'.format(i).upper().rjust(2),'{:0b}'.format(i).rjust(2))
    
    #ATQ :  Each value should be space-padded to match the width of the binary value of n.
    print(str(i).rjust(w,' '),'{:0o}'.format(i).rjust(w,' '),'{:0x}'.format(i).upper().rjust(w,' '),'{:0b}'.format(i).rjust(w,' '))
    
    
    