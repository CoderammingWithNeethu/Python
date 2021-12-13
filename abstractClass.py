from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod #need to define display method in all inherited classes
    def display(): 
        pass

class MyBook(Book):
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):  #abstract function defination 
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Price: {self.price}')


title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()