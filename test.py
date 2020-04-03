#!/usr/bin/python3.6

import sys
sys.setrecursionlimit(10000)


import ModRing
from ModRing import IntegerModRing
from numpy import random

from sympy import *

import Dictionary
import RSA

import Prime



# RSA.example()
# Dictionary.example()

# print(Prime.miller(nextprime(2**10000000000), 100))
# print(Prime.baseMiller(3, 2))

print(Prime.prime(5000))
