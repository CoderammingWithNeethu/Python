#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    bi = bin(n).strip('0b').split('0')
    #mn = max([len(i) for i in bi])
    mn = max(map(len,bi))
    #print(bi)
    print(mn)