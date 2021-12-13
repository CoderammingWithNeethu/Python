import time
from functools import lru_cache #decorator

@lru_cache(maxsize=3) #caches latest 3 instances of the function
def some_work(n):
    time.sleep(n)
    print(n)
    return n

if __name__ == '__main__':
    print('Running some work...')
    some_work(3)
    #some_work(2) #wud have saved thes below 3 values in cache due to maxsize 
    #some_work(5)
    #some_work(1)
    print('Done.. Running Again')
    some_work(3) #dont have to wait here again for 3 seconds after cache
    print('Done')
