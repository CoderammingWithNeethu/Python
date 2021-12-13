
from copy import copy, deepcopy
'''
list1 = [1,2,[3,5],4]
list2 = deepcopy(list1)
list2[3]=7
list2[2].append(6)
print(list1)
print(list2)
'''

l1 = [1,2,3,4,5,[9,7]]
l2 = l1.copy()
#l2 = deepcopy(l1)
l2[2]=7
print(l1)
print(l2)
'''
l1 = [1, 2, 3]
l2 = l1
l3 = l1.copy()
l4 = list(l1)
l1[0] = [7]
print(l1, l2, l3, l4)

[[7], 2, 3] [[7], 2, 3] [1, 2, 3] [1, 2, 3]
'''