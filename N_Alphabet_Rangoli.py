# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:31:24 2020

@author: nnath
"""

'''
You are given an integer, N. Your task is to print an alphabet rangoli of size N. 

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

'''
'''
THEORY : 
character to int : chr(number)

int to character : ord(number+) #ord(character) expected a character i.e. string of length one
ord('A') -> 65 ; ord('Z') -> 90
ord('a') -> 97 ; ord('z') -> 122
'''
n = int(input())
for i in range(n):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))

for i in range(n-1):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))