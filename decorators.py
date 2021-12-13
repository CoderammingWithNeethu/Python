def names_decorators(function):
    def wrapper(arg1,arg2):
        print('wrapper function')
        arg1 = arg1.capitalize()
        arg2 = arg2.upper()
        string_hello = function(arg1,arg2)
        return string_hello
    return wrapper

@names_decorators
def say_hello(name1,name2):
    print('say_hello function')
    return 'Hello '+name1+' Hello '+name2

a = say_hello('sara', 'ali')
print(a)