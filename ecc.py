p = 17
a = 2
G = (5, 1)

def add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1+y2)%p == 0:
        return None

    if P == Q:
        m = (3*x1*x1+a)*pow(2*y1, -1, p)%p
    else:
        m = (y2-y1)*pow((x2-x1)%p, -1, p)%p

    x3 = (m*m-x1-x2)%p
    y3 = (m*(x1-x3)-y1)%p

    return (x3, y3)


def mul(k, P):
    R = None

    while k:
        if k%2:
            R = add(R, P)

        P = add(P, P)
        k //= 2

    return R


def encrypt(M, Q):
    k = 3
    C1 = mul(k, G)
    C2 = add(M, mul(k, Q))
    return C1, C2


def decrypt(C1, C2, d):
    S = mul(d, C1)
    neg = (S[0], -S[1]%p)
    return add(C2, neg)


# Key generation
d = 7
Q = mul(d, G)

# Message point
M = (6, 3)

ct = encrypt(M, Q)

print("Public key:", Q)
print("Private key:", d)
print("Encrypted:", ct)
print("Decrypted:", decrypt(ct[0], ct[1], d))