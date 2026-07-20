from math import gcd

# Check prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Extended Euclidean Algorithm
def mod_inverse(e, phi):
    def egcd(a, b):
        if b == 0:
            return (a, 1, 0)
        g, x1, y1 = egcd(b, a % b)
        return (g, y1, x1 - (a // b) * y1)
    g, x, y = egcd(e, phi)
    return x % phi if g == 1 else None

# Input
print("Enter prime numbers")
while True:
    p = int(input("Enter p: "))
    q = int(input("Enter q: "))

    if not is_prime(p) or not is_prime(q):
        print("Both numbers must be prime.\n")
        continue
    if p == q:
        print("p and q must be different.\n")
        continue
    n = p * q
    if n <= 255:
        print("Choose larger prime numbers (p × q > 255).\n")
        continue
    break

# Key Generation
phi = (p - 1) * (q - 1)
e = 3
while gcd(e, phi) != 1:
    e += 2
d = mod_inverse(e, phi)
print("\nPublic Key :", (e, n))
print("Private Key:", (d, n))

# Message Input
while True:
    msg = input("\nEnter Message: ")
    if msg:
        break
    print("Message cannot be empty.")
# Encryption
cipher = [pow(ord(ch), e, n) for ch in msg]
print("\nEncrypted Message:", cipher)
# Decryption
plain = ''.join(chr(pow(c, d, n)) for c in cipher)
print("Decrypted Message:", plain)









