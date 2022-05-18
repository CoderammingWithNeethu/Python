#import go own their own lines
import sys
import os

#PEP :Python Enhancement Proposals ---> Guideline for Python Code  
'''
*************PEP****************
'''
#two blank lines separate classes from other functions
class MyClass():
    def __init__(self):
        self.prop1 = "myclass"

    #within the class one blank line separates method
    def method1(self,arg1):
        pass

def main():
    #79 lines of code 
    #72 long comments
    cls1 = MyClass()
    cls1.prop1 = "hello world"