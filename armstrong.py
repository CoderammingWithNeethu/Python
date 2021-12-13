'''
x =0
ii=153
import ipdb; ipdb.set_trace()
for i in str(ii):
    x += int(i)**3
if x == ii :
    s = 'It is an ARMSTRONG number'
else :
    s = "It is NOT an ARMSTRONG number"
print(s)
'''

from random import random
def fun(x=random()):
    print(x)

fun()
fun()