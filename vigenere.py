def encrypt(pt, key):
    res = ""
    key = key
    j = 0

    for ch in pt:
        if ch.isalpha():
            k = ord(key[j%len(key)])-65
            res+= chr((ord(ch)-65+k)%26+65)
            j+=1
        else:
            res+=ch

    return res

def decrypt(pt, key):
    res = ""
    key = key
    j = 0

    for ch in pt:
        if ch.isalpha():
            k = ord(key[j%len(key)])-65
            res+= chr((ord(ch)-65-k)%26+65)
            j+=1
        else:
            res+=ch

    return res

pt = input("Plain text: ")
key = input("Key: ")

ct = encrypt(pt, key)
print("Encrypted:", ct)
print("Decrypted:", decrypt(ct, key))