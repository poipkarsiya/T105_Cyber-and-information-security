# ==========================================
# DIFFIE-HELLMAN KEY EXCHANGE - CLI
# ==========================================

def diffie_hellman():
    print("=" * 50)
    print("      DIFFIE-HELLMAN KEY EXCHANGE")
    print("=" * 50)

    p = int(input("Enter a prime number (p): "))
    g = int(input("Enter a primitive root (g): "))

    print("\nPublic Parameters:")
    print("Prime number (p) =", p)
    print("Primitive root (g) =", g)

    siya = int(input("\nEnter private key of Siya: "))
    jay = int(input("Enter private key of Jay: "))

    S = pow(g, siya, p)
    J = pow(g, jay, p)

    print("\n--- Key Generation ---")
    print("Siya's Private Key =", siya)
    print("Jay's Private Key   =", jay)
    print("\nSiya's Public Key =", S)
    print("Jay's Public Key   =", J)

    siya_key = pow(J, siya, p)
    jay_key = pow(S, jay, p)

    print("\n--- Shared Secret Key ---")
    print("Siya calculates:", siya_key)
    print("Jay calculates  :", jay_key)

    if siya_key == jay_key:
        print("\n✓ Key exchange successful!")
        print("✓ Both entities have the same shared secret key.")
    else:
        print("\n✗ Key exchange failed.")

    print("\n" + "=" * 50)


diffie_hellman()
