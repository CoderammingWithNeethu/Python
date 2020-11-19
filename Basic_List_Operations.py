# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 12:56:01 2020

@author: nnath
"""

'''
PROBLEM STATEMENT :
    
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the  types listed above
'''
n = int(input('Enter number of operations : '))
lst = []

def op(a):
    if a[0] == 'insert':
        lst.insert(int(a[1]),int(a[2]))
    elif a[0] == 'print':
        print(lst)
    elif a[0] == 'remove':
        lst.remove(int(a[1]))
    elif a[0] == 'append':
        lst.append(int(a[1]))
    elif a[0] == 'sort':
        lst.sort()#inplace but sorted(lst) - creates a new sorted lst
    elif a[0] == 'pop':
        lst.pop()
    elif a[0] == 'reverse':
        lst.reverse()
    else:    
        print('Didnt understand')
    #return lst
    

for i in range(n):
    a  = input('Enter operation : ').split()
    op(a)
    
    