import itertools

def testFunction(x):
    return x < 40

def main():

    #Cycle function of itertool to cycle over a collection
    names = ['Neethu','Geethu','Arya']
    nam = itertools.cycle(names)
    print(next(nam))
    print(next(nam))
    print(next(nam))
    print(next(nam))#repeats like a cycle

    #count
    count1 = itertools.count(100,10)
    print(next(count1))
    print(next(count1))
    print(next(count1))

    #Accumulate function to aggregate value -- running addition of numbers that came before
    vals = [10,20,30,40,50,20,10]
    acc = itertools.accumulate(vals)
    print(list(acc))#[10, 30, 60, 100, 150, 170, 180]

    acc2 = itertools.accumulate(vals,max)#when max value reached keeps repeating the value 
    print(list(acc2))#[10, 20, 30, 40, 50, 50, 50]

    #chain function 
    x = itertools.chain('ABCD','1234')
    print(list(x))#chains the 2 given sequences 

    #Dropwhile and takewhile will return values until a certain condition is met that stops them 
    print(list(itertools.dropwhile(testFunction, vals)))#skips the values till vals
    print(list(itertools.takewhile(testFunction, vals)))#returns the values until vals 


if __name__ == '__main__':
    main()