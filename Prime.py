from numpy import random
from ModRing import IntegerModRing

def baseMiller(n, a):
    """returns True if n passes the Miller test in a-base"""
    ring = IntegerModRing(n)

    N = n-1
    s = 0
    while N%2 == 0:
        N = N//2
        # d = 2*d
        s += 1
    d = (n-1)//(ring.pow(2, s))

    x = ring.pow(a, d)
    if x == 1 or x == n-1 :
        return True
    else :
        for i in range(s-1) :
            x = ring.pow(x, 2)
            if x == n-1:
                return True
    return False


def miller(n, m):
    """Returns True if n passes the Miller test in m bases"""

    if n==0 or n==1:
        return False

    lenN = getLen(n)
    for i in range(m):
        a = n
        while a >= n or a == 0:
            a = randomBytes(lenN)
        if not baseMiller(n, a):
            return False
    return True
    

def randomBytes(n):
    """Returns a random number of n bits"""

    number = 0
    for i in range(n):
        a = random.randint(0, 2)
        number = number + a * 2**i
    return number

def randomBytesStrict(n):
    """Returns a random number of strictly n bits"""

    number = 2**(n-1)
    for i in range(n-1):
        a = random.randint(0, 2)
        number = number + a * 2**i
    return number

def getLen(n):
    """Returns the number of bits of n"""
    cpt = 1
    while(n>1):
        n = n//2
        cpt+=1
    # print(cpt)
    return cpt

def prime(k):
    """Returns a prime number on k bits"""

    ok = False
    while not ok:
        x = randomBytesStrict(k)
        test = miller(x, 100)
        if test:
            return x



