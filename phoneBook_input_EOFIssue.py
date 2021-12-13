
n = int(input())
dt_name_ph = {}
for _ in range(n):
    name_ph = input()
    a = name_ph.split()
    dt_name_ph[a[0].strip()]=a[1].strip()
    
#print(dt_name_ph)
name_search_list = []
name_search = None

try :
    while name_search != '':
        name_search = input().strip() #The problem with input is that it would raise an EOFError when there is not more inputs left to be read. (NOTE : this is while loop)
        #Rather than using input, consider using sys.stdin.readline().strip() which returns an empty string '' during an EOF situation
        name_search_list.append(name_search)

    name_search_list.remove('')
    #print(name_search_list)

    for name in name_search_list:
        ph = dt_name_ph.get(name,'Not found')
        if ph != 'Not found':
            print(name+'='+ph)
        else:
            print(ph)

except(EOFError):
    pass



'''
Solution 1 :

N=int(input())
phoneBook={}

for _ in range(N):
    name,contact=input().split()
    phoneBook[name]=contact

try:
    while(True):
        check=str(input())
        if check in phoneBook:
            print(check+"="+phoneBook[check])
        else:
            print('Not found')

except(EOFError):
    pass



Solution 2 :

import sys 

# Read input and assemble Phone Book
n = int(input())
phoneBook = {}
for i in range(n):
    contact = input().split(' ')
    phoneBook[contact[0]] = contact[1]

# Process Queries
lines = sys.stdin.readlines()  # convert lines to list
for i in lines:
    name = i.strip()
    if name in phoneBook:
        print(name + '=' + str( phoneBook[name] ))
    else:
        print('Not found')
'''