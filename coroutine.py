def searcher():
    import time
    print('Book Reading')#printed only once 
    # 4 sec task execution 
    book = 'This is a lengthy book taking too much time'
    time.sleep(4)

    #for every other call starts from here - coroutine
    while True:
        text =(yield)
        if text in book:
            print('text in book')
        else:
            print('Text not in book')

search = searcher()
print('Search Started')
next(search)#1st time takes time to load then for all search call directly runs from while loop 
#just like 1 time loading data e.g. in AI/ML then using the data for the functions 

print('Next method started')
search.send("time")
input('Press any key')
search.send('book')
input('Press any key')
search.send('hey')

search.close()#release all resources