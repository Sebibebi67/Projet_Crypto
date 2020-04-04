import Prime


def prime(k):
    while True:
        q = Prime.prime(k)
        p = 2*q+1
        test = Prime.miller(p, 100)
        if test:
            return p