#use transform functions like sorted, filter, map

def filterFunc(x):
    if x % 2 == 0:
        return False
    return True

def filterFunc2(x):
    if x.isupper():
        return False
    return True

def squareFunc(x):
    return x**2

def toGrade(x):
    if(x >= 90):
        return 'A'
    elif (x >= 80 and x < 90):
        return 'B'
    elif (x >= 70 and x < 80):
        return 'C'
    elif (x >= 60 and x < 70):
        return 'D'
     
    return 'F'

def main():
    nums = (1,8,4,5,13,26,381,410,58,47)
    chars = 'abcDeFGHiJklmnoP'
    grades = (81,89,94,78,61,66,99,74)

    #use filter to remove items from the list
    odds = list(filter(filterFunc,nums))
    print(odds)
    print('-'*10)
    lowers = list(filter(filterFunc2, chars))
    print(lowers)
    print('-'*10)

    #Using map function 
    squares = list(map(squareFunc,nums))
    print(squares)
    print('-'*10)

    grades = sorted(grades)
    letters = list(map(toGrade,grades))
    print(grades)
    print(letters)

if __name__ == '__main__':
    main()


'''
Filter function: Creates an iterator that filters out value from  a given sequence ; you pass a func to perform a test and if the test returns false then the item is removed from the resulting sequence 

Map Function: Creates iterator that takes one or more sequences of values to produce a new sequence by applying a given function to each value in the original sequence 
'''