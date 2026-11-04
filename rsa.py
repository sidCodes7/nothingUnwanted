def encrypt(pt, e, n):
    res = []

    for ch in pt:
        res.append(pow(ord(ch),e,n))
    return res

def decrypt(ct, d, n):
    res = ""

    for x in ct:
        res+= chr(pow(x, d, n))
    return res

p = 61
q = 53

n = p*q
phi = (p-1)*(q-1)

e = 17
d = pow(e, -1, phi)

pt = input("Plain text: ")

ct = encrypt(pt, e, n)

print("Public key:", (e, n))
print("Private key:", (d, n))
print("Encrypted:", ct)
print("Decrypted:", decrypt(ct, d, n))