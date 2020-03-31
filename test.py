#!/usr/bin/python3.6


from sympy import *
import ModRing
from ModRing import IntegerModRing

import Euclide

import Dictionary

# message = "HelloWorld"
# print(message)

# codedMessage = Dictionary.encodageBloc(message)
# print(codedMessage)

# decodedMessage = Dictionary.decodageBloc(codedMessage)
# print(decodedMessage)


message = "Hello world, today we will learn how to code a message which could be as long as u want"
print(message)

L = Dictionary.encode(message)
print(L)

decodedMessage = Dictionary.decode(L)
print(decodedMessage)



