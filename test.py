#!/usr/bin/python3.6


from sympy import *
import Annexe
from Annexe import IntegerModRing







a = IntegerModRing(25)

x = a.pow(16, 2345677)
print(x)

y = a.pow(17, -1)
print(y)


# print(z)






