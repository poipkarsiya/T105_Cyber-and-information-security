#CLI
import hmac
import hashlib

# Take input from user
key = input("Enter Secret Key: ").encode()
message = input("Enter Message: ").encode()

# Generate MAC
mac = hmac.new(key, message, hashlib.sha256).hexdigest()

print("\nOriginal Message:", message.decode())
print("Generated MAC:", mac)

# Verify MAC
received_message = input("\nEnter Message Again for Verification: ").encode()
received_mac = input("Enter MAC for Verification: ")

calculated_mac = hmac.new(
    key,
    received_message, 
    hashlib.sha256
).hexdigest()

if hmac.compare_digest(received_mac, calculated_mac):
    print("\nMAC Verification: Successful")
    print("Message is authentic and has not been modified.")
else:
    print("\nMAC Verification: Failed")
    print("Message may have been modified.")



