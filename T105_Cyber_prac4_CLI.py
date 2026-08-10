# Practical 4: Digital Signature using RSA

import hashlib
import math

def generate_keys():
    p, q = 61, 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def create_signature(message, private_key):
    d, n = private_key
    h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    return pow(h, d, n)

def verify_signature(message, signature, public_key):
    e, n = public_key
    h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    return pow(signature, e, n) == h % n


print("==============================================")
print("       RSA DIGITAL SIGNATURE PROGRAM")
print("==============================================")

public_key, private_key = generate_keys()

print("\nPublic Key :", public_key)
print("Private Key:", private_key)

message = input("\nEnter the message: ")

print("\nOriginal Message:")
print(message)

signature = create_signature(message, private_key)

print("\nDigital Signature:")
print(signature)

result = verify_signature(message, signature, public_key)

if result:
    print("\nSignature Verification: SUCCESS")
    print("Message is authentic and has not been modified.")
else:
    print("\nSignature Verification: FAILED")
    print("Message may have been modified.")

print("\n----------------------------------------------")
print("Testing message integrity")
print("----------------------------------------------")

modified_message = input("Enter modified message: ")

result2 = verify_signature(modified_message, signature, public_key)

if result2:
    print("\nModified Message Verification: SUCCESS")
    print("Message is authentic.")
else:
    print("\nModified Message Verification: FAILED")
    print("Message has been modified or signature is invalid.")

print("\n==============================================")
print("             PROGRAM COMPLETED")
print("==============================================")
