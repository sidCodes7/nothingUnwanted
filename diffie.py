p = 23
g = 5

# Private keys
a = 6
b = 15

# Public keys
A = pow(g, a, p)
B = pow(g, b, p)

# Shared secret keys
KA = pow(B, a, p)
KB = pow(A, b, p)

print("Alice's public key:", A)
print("Bob's public key:", B)

print("Alice's shared key:", KA)
print("Bob's shared key:", KB)