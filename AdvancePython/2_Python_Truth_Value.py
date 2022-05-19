'''
***********Python Truth Value*************
'''
#False and None evaluates to false
#Numeric zero values: 0,0.0,0j also evaluates to false
#Decimal(0), Fraction(0,x) also evaluates to false
#Empty sequences/collection evaluates to fralse : '',(),[],{}

x = []
print(bool(x)) #Output: False 

#Empty sets and range: set(), range(0) are also boolean false
#For custom object are by default True unless override the bool function and return a False value or overrise a len function and return a 0 value (as shown below)

class myClass:
    def __bool__(self):
        return False
        
    def __len__(self):
        return 0

'''
Boolean Operations
'''
#AND, OR, NOT
