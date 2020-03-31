#!/usr/bin/python3.6


from sympy import *
import ModRing
from ModRing import IntegerModRing

import Euclide




# a = Euclide.simpleIt(47997435, 355714785)
# b = Euclide.simpleRec(47997435, 355714785)
# print(a, b)


(i, j) = (45, 63)
(x, y, z) = Euclide.etenduIt(i, j)
(x2, y2, z2) = Euclide.etenduRecInit(i, j)
print(x, y*i+j*z)
print(x2, y2*i+j*z2)





# a = IntegerModRing(25)

# x = a.pow(16, 2345677)
# print(x)

# y = a.pow(17, -1)
# print(y)


# print(z)






