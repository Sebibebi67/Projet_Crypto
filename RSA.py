from sympy import *
from numpy import random

import Dictionary

from ModRing import IntegerModRing

def createPrime():
    p = randprime(10**20, 10**21)
    return p

def calculatingPhi(p, q):
    return (p-1)*(q-1)

def newRandom(x):
    newPrime = randprime(2, x)
    while(newPrime%x == 0):
        newPrime = randprime(2, x)
    return newPrime


def encryption(x, n, a):
    """returns x^a mod n"""
    ring = IntegerModRing(n)
    return ring.pow(x, a)


def example():
    print("------Testing RSA------")
    print("\n\n")

    print("------Creating p & q------")
    p = createPrime()
    q = createPrime()
    print("p = ", p)
    print("q = ", q)
    print("\n\n")

    print("------Calculating n------")
    n = p*q
    print("n = ", n)
    print("\n\n")

    print("------Calculating Phi(n)------")
    phi = calculatingPhi(p, q)
    print("phi(n) = ", phi)
    print("\n\n")

    b = 0
    while b == 0:

        print("------Finding a random which is prime with Phi(n)------")
        a = newRandom(phi)
        print("a = ", a)
        print("\n\n")

        print("------Calculating b=a^(-1) mod phi(n)------")
        ring = IntegerModRing(phi)
        b = ring.pow(a, -1)
        print("b = ", b)
        print("\n\n")

    print("------Encoding the message------")
    message = "Today, we are going to learn how to programm RSA in python3.6"
    print("uncoded message : ", message)
    print("\n\n")

    L=Dictionary.encoding(message)
    print(L)
    L2 = []
    for _ in L:
        L2.append(encryption(_, n, a))
        # print(L2)
    print("coded message : ", L2)
    print("\n\n")

    print("------Decoding the message------")
    L3 = []
    for _ in L2:
        L3.append(encryption(_, n, b))
    decodedMessage = Dictionary.decoding(L3)
    print("decoded message : ", decodedMessage)
    print("\n\n")


    



