

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


class IntegerModRing:

    mod = 0

    def __init__(self, n = 1):
        self.mod = n

    def pow(self, x, a):
        """return x^a mod n"""

        if a<-1:
            print("error : ", a, " <-1")
            return 0
        elif a == -1:
            return invModul(x, self.mod)
        else :
            if a%2 == 0 :
                y = pow(x, a//2)%self.mod
                return y*y%self.mod
            else :
                y = pow(x, a//2)%self.mod
                return x*y*y%self.mod

    def add(self, x, y):
        """return x + y mod n"""
        return (x+y)%self.mod

    def prod(self, x, y):
        """return x*y mod n"""
        return (x*y)%self.mod


# class PolynomialRing:
        
