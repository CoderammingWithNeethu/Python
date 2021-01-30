# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 09:04:10 2020

@author: nnath
"""

s = '0123456789'
s[2:8:-1]#empty; from index 2 toward left , no index 8 found 
s[6:1:-1]#go left to right start from 6 go till 0 ----go till 0???? but end+1 = 2
s[6:1:-2]#go left to right skipping 2 start from 6(-2)..4(-2)..2 ----go till 0???? but end+1 = 2
s[-1:-6:1]#empty string
s[-1:-6:-1]#gor left to right start from -1 go till -6+1(-ve)
s[-1:6:-1]#gor left to right start from -1 go till 6+1(-ve)