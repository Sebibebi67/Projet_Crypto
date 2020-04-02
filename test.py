#!/usr/bin/python3.6


from sympy import *
import ModRing
from ModRing import IntegerModRing

import Euclide
import Dictionary
import RSA

# message = "HelloWorld"
# print(message)

# codedMessage = Dictionary.encodageBloc(message)
# print(codedMessage)

# decodedMessage = Dictionary.decodageBloc(codedMessage)
# print(decodedMessage)


# message = "Hello world, today we will learn how to code a message which could be as long as u want"
# message = "Inserer ici n'importe quelle phrase, quelle soit valide ou non, a votre convenance"
# print(message)

# L = Dictionary.encode(message)
# print(L)

# decodedMessage = Dictionary.decode(L)
# print(decodedMessage)

# p = RSA.createPrime()
# q = RSA.createPrime()

# n = p*q

# print(p, q, n)


RSA.example()
