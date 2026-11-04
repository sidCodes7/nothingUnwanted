def encrypt(pt, k):
    res = ""

    for ch in pt:
        res += chr((ord(ch)-65+k)%26+65)

    return res

def decrypt(ct, k):
    return encrypt(ct, -k)

pt = input("Plain text: ")
k = int(input("key: "))

ct = encrypt(pt, k)
print(ct)
print(decrypt(ct, k))