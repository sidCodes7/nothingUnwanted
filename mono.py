def encrypt(pt, k):
    res = ""

    for ch in pt:
        if ch.isupper():
            res+= k[ord(ch)-65]
        else:
            res+=ch

    return res

def decrypt(ct, k):
    res = ""
    for ch in ct:
            if ch.isupper():
                res+= chr(k.index(ch)+65)
            else:
                res+=ch
    
    return res

key = "QWERTYUIOPASDFGHJKLZXCVBNM"

pt = input("Plain text: ").upper()

ct = encrypt(pt, key)
print("Encrypted:", ct)
print("Decrypted:", decrypt(ct, key))