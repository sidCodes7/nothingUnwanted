def encrypt(pt, y, g, p):
    res = []

    for ch in pt:
        m = ord(ch)
        k = 3
        c1 = pow(g,k,p)
        c2 = (m*pow(y,k,p))%p
        res.append((c1,c2))
    return res

def decrypt(ct, x, p):
    res = ""

    for c1,c2 in ct:
        s = pow(c1, x, p)
        m = (c2*pow(s, -1, p))%p
        res+=chr(m)

    return res

p = 467
g = 2
x = 127

y = pow(g, x, p)

pt = input("Plain text: ")

ct = encrypt(pt, y, g, p)

print("Public key:", (p, g, y))
print("Private key:", x)
print("Encrypted:", ct)
print("Decrypted:", decrypt(ct, x, p))