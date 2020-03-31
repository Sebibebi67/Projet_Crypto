import Euclide

class IntegerModRing:
    """ Initialize a Integer Ring like a = IntegerModRing(25)
        Then you can work in your ring :
        for example, you can use calculate a.pow(2, 6) which calculates 2^6 mod 25"""

    mod = 0

    def __init__(self, n = 1):
        self.mod = n

    def pow(self, x, a):
        """return x^a mod n"""

        if a<-1:
            print("error : ", a, " <-1")
            return 0
        elif a == -1:
            return Euclide.invModul(x, self.mod)
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
        
