# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:51:47 2020

@author: nnath
"""

'''
PROBLEM STATEMENT :
    
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be N*M. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
'''
#length,breadth =int(input('Enter Length : ')), int(input('Enter Breadth : '))
a = input().split()
length,breadth = eval(a[0]),eval(a[1])
if breadth == 3*length:
    k =1
    for i in range(1,((length+1)//2)):
        print((k*'.|.').center(breadth,'-'))
        k+=2
    print('WELCOME'.center(breadth,'-'))
    for j in range((length//2),0,-1):
        k-=2
        print((k*'.|.').center(breadth,'-'))    
    
    