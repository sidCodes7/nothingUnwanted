def encrypt(pt, key):
    res = ""
    pt = pt.upper().replace(" ", "")

    if len(pt) % 2:
        pt += "X"

    for i in range(0, len(pt), 2):
        a = ord(pt[i])-65
        b = ord(pt[i+1])-65

        x = (key[0][0]*a + key[0][1]*b)%26
        y = (key[1][0]*a + key[1][1]*b)%26

        res+= chr(x+65) + chr(y+65)

    return res

def decrypt(ct, key):
    det = (key[0][0]*key[1][1] - key[0][1]*key[1][0])%26
    inv = pow(det, -1, 26)

    inv_key = [
        [key[1][1]*inv%26, -key[0][1]*inv%26],
        [-key[1][0]*inv%26, key[0][0]*inv%26]
    ]

    return encrypt(ct, inv_key)

key = [[3, 3], [2, 5]]

pt = input("Plain text: ")

ct = encrypt(pt, key)

print("Encrypted:", ct)
print("Decrypted:", decrypt(ct, key))
