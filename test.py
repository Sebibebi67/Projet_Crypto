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
import ElGamal



# RSA.example()
# Dictionary.example()

print(ElGamal.prime(500))
