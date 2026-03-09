from data import *

def legendre_symbol(a, p):
    if a % p == 0:
        return 0
    return pow(a, (p - 1) // 2, p)

def is_quadratic_residue(a, p):
    symbol = legendre_symbol(a, p)
    return symbol == 1


def modular_sqrt(a, p):
    if not is_quadratic_residue(a, p):
        return None

    # Special case for p ≡ 3 (mod 4)
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    # Otherwise use Tonelli-Shanks algorithm
    s, t = p - 1, 0
    while s % 2 == 0:
        s //= 2
        t += 1

    # Find a non-residue z
    z = 2
    while legendre_symbol(z, p) != -1:
        z += 1

    m = t
    c = pow(z, s, p)
    r = pow(a, (s + 1) // 2, p)
    t = pow(a, s, p)
    while t != 1:
        t2i = t
        for i in range(1, m):
            t2i = pow(t2i, 2, p)
            if t2i == 1:
                break
        b = pow(c, 2**(m - i - 1), p)
        m = i
        c = pow(b, 2, p)
        t = (t * c) % p
        r = (r * b) % p

    return r

for i in liste :
    x = modular_sqrt(i,p)
    if x : 
        print("\n", pow(i, 1/2))
        f = open("file.txt","w")
        f.write(str(f"{i}\n\n")) ; f.write(str(x))