def simpleIt(a, b):
    (r0, r1) = (a, b)
    while r1!=0:
        (r0, r1) = (r1, r0%r1)
    return r0


def simpleRec(a, b):
    r = a%b
    if r!=0:
        return simpleRec(b, a%b)
    else:
        return b
    

def extendedIt(a, b):
    (r0,r1) = (a, b)
    (u0, u1) = (1, 0)
    (v0, v1) = (0, 1)

    while r1!=0:
        q = r0//r1
        (r0, r1) = (r1, r0 - q * r1)
        (u0, u1) = (u1, u0 - q * u1)
        (v0, v1) = (v1, v0 - q * v1)
    return r0, u0, v0

def extendedRecInit(a, b):
    return extendedRec(a, b, 1, 0, 0, 1)

def extendedRec(a, b, u0, u1, v0, v1):
    (r0,r1) = (a, b)

    if r1!=0:
        q = r0//r1
        (r0, r1) = (r1, r0 - q * r1)
        (u0, u1) = (u1, u0 - q * u1)
        (v0, v1) = (v1, v0 - q * v1)
        return extendedRec(r0, r1, u0, u1, v0, v1)
    else:
        return r0, u0, v0
    

def revModul(a, n):
    """reverse a modulo n"""
    q = 0
    (r0,r1) = (n,a)
    (v0,v1) = (0,1)

    while r1 != 0 :
        q = r0//r1

        (r0,r1) = (r1,r0-r1*q)
        (v0,v1) = (v1,v0-v1*q)

    if r0 != 1:
        print (a, " is not reversible modulo ", n)
        return 0
    else:
        print (a, " is reversible modulo ", n)
        return v0%n

