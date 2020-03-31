def simpleIt(a, b):
    (r0, r1) = (a, b)
    while r1!=0:
        (r0, r1) = (r1, r0%r1)
    return r0


def simpleRec(a, b):
    r= a%b
    if r!=0:
        return simpleRec(b, a%b)
    else:
        return b
    

# def etenduIt(a, b):


# def etenduRec(a, b):
    







def invModul(a, n):
    """inverse a modulo n"""
    q = 0
    (r0,r1) = (n,a)
    (v0,v1) = (0,1)

    while r1 != 0 :
        q = r0//r1

        (r0,r1) = (r1,r0-r1*q)
        (v0,v1) = (v1,v0-v1*q)

    if r0 != 1:
        print (a, " n'est pas inversible modulo ", n)
        return 0
    else:
        print (a, " est inversible modulo ", n)
        return v0%n

