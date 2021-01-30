# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:27:23 2020

@author: nnath
"""
'''
PROBLEM STATEMENT 1: SUM and LEN FUNCTION
average = sum of distinct of values / number od distinct values
 
'''
def average(array):
    #sum(set(array))/set(array).__len__()
    return sum(set(array))/len(set(array))
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    
    
'''
PROBLEM STATEMENT 2: SET ADD FUNCTION

    The first line contains an integer N, the total number of country stamps.
    The next N lines contains the name of the country where the stamp is from. 
    Find the total number of distinct country stamps.

'''
num_stamp = int(input('Enter no country stamps : '))
x=1
distinct_stamp=set()
while x<=num_stamp:
    distinct_stamp.add(input())#add() returns none
    x+=1
print(len(distinct_stamp))

'''
PROBLEM STATEMENT 3: SET -- REMOVE, DISCARD, POP FUNCTION
    The first line contains integer n , the number of elements in the set s. 
    The second line contains n space separated elements of set s. 
    All of the elements are non-negative integers, less than or equal to 9. 
    The third line contains integer N, the number of commands.
    The next N lines contains either pop, remove and/or discard commands followed by their associated value.
    
    print the sum of element in the set
'''
#.remove(value) -- raise error if value not present else deletes value in set
#.discard(value) -- do not raise error if value not present else deletes value in set
#.pop() --randomdly delete the value

num_ele = int(input('Enter number of elements to enter: '))

set_3 = input().split()
set_3 = set(set_3[:num_ele+1])
print(set_3)
#s = set(map(int, input().split()))
#set_3 = set([input() for i in range(num_ele)])
'''
while x<=num_ele:
    set_3.add(input())
    x+=1
'''    
num_func = int(input('Enter number of functions to enter: '))
y=1
while y<=num_func:
    i = input().split()
    
    if i[0] == 'pop':
        set_3.pop()
        
    elif i[0] == 'remove':
        i[1]=int(i[1])
        set_3.remove(i[1])
        
    elif i[0] == 'discard':
        i[1]=int(i[1])
        set_3.discard(i[1])
        
    else:
        print('Function not recognized')
    y+=1
print(sum(set_3))

'''
PROBLEM STATEMENT 4: UNION(), INTERSECTION(), DIFFERENCE(), SYMMETRIC_DIFFERENCE()
    The students of District College have subscriptions to English and French newspapers. 
    Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
    You are given two sets of student roll numbers. 
    One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. 
    The same student could be in both sets. 
    
    i)Your task is to find the total number of students who have subscribed to at least one newspaper.
    ii)Your task is to find the total number of students who have subscribed to both newspapers.
    iii)Your task is to find the total number of students who have subscribed to only English newspapers.
    iv)Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.
'''
#A.union(B) , A|B
#A.intersection(B), A&B
#A.difference(B), A-B
#A.symmetric_difference(B), A^B

no_A = int(input())
set_A = set(map(int, input().split()[:no_A+1]))#calls the specified function for each item of an iterableand returns a list of results.

no_B = int(input())
set_B = set(map(int, input().split()[:no_B+1]))

print(len(set_A|set_B))#at least one newspaper
print(len(set_A&set_B))#both newspapers
print(len(set_A-set_B))#only Eng newspaper
print(len(set_B-set_A))#only French newspaper
print(len(set_A^set_B))#only one newspaper; exclude intersection


'''
PROBLEM STATEMENT 5: SET MUTATION
    
    
'''