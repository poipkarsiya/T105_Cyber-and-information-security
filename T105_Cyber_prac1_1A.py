#1 Caesar Cipher CLI
def cipher(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + key) % 26 + base)
        else:
            result += ch
    return result

while True:
    print("\n--- Caesar Cipher ---")
    print("1. Encrypt\n2. Decrypt\n3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        text = input("Enter Plain Text: ")
        key = int(input("Enter Key: "))
        print("Encrypted Text:", cipher(text, key))

    elif choice == "2":
        text = input("Enter Cipher Text: ")
        key = int(input("Enter Key: "))
        print("Decrypted Text:", cipher(text, -key))

    elif choice == "3":
        break

    else:
        print("Invalid Choice")
        print("-------------------------------------------------")



#2 Monoalphabetic Cipher CLI
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

key = "QWERTYUIOPASDFGHJKLZXCVBNM"

def convert(text, frm, to):
    result = ""
    for ch in text.upper():
        result += to[frm.index(ch)] if ch in frm else ch
    return result

while True:
    print("\n--- Monoalphabetic Cipher ---")
    print("1. Encrypt\n2. Decrypt\n3. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        text = input("Enter Plain Text: ")
        print("Encrypted Text:", convert(text, alphabet, key))

    elif ch == "2":
        text = input("Enter Cipher Text: ")
        print("Decrypted Text:", convert(text, key, alphabet))

    elif ch == "3":
        break

    else:
        print("Invalid Choice")




#1 Caesar Cipher GUI
from tkinter import *

def cipher(shift):
    text = msg.get()
    key = int(k.get()) * shift
    result = ""

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + key) % 26 + base)
        else:
            result += ch

    out.config(state="normal")
    out.delete(0, END)
    out.insert(0, result)
    out.config(state="readonly")

root = Tk()
root.title("Caesar Cipher")
root.geometry("420x220")
root.configure(bg="#EAF4FC")
root.resizable(False, False)

Label(root, text="Caesar Cipher", font=("Arial", 16, "bold"),
      bg="#EAF4FC", fg="navy").grid(row=0, column=0, columnspan=2, pady=10)

Label(root, text="Message:", bg="#EAF4FC",
      font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=8, sticky="e")
msg = Entry(root, width=30, font=("Arial", 11))
msg.grid(row=1, column=1)

Label(root, text="Key:", bg="#EAF4FC",
      font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=8, sticky="e")
k = Entry(root, width=10, font=("Arial", 11))
k.grid(row=2, column=1, sticky="w")

Button(root, text="Encrypt", bg="#4CAF50", fg="white",
       width=12, command=lambda: cipher(1)).grid(row=3, column=0, pady=15)

Button(root, text="Decrypt", bg="#2196F3", fg="white",
       width=12, command=lambda: cipher(-1)).grid(row=3, column=1)

Label(root, text="Result:", bg="#EAF4FC",
      font=("Arial", 11)).grid(row=4, column=0, padx=10, sticky="e")
out = Entry(root, width=30, font=("Arial", 11), state="readonly")
out.grid(row=4, column=1)

root.mainloop()



#2 Monoalphabetic Cipher GUI
from tkinter import *

A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
K = "QWERTYUIOPASDFGHJKLZXCVBNM"

def run(enc):
    frm, to = (A, K) if enc else (K, A)
    text = msg.get().upper()
    ans = ''.join(to[frm.index(c)] if c in frm else c for c in text)
    out.config(state="normal")
    out.delete(0, END)
    out.insert(0, ans)
    out.config(state="readonly")

root = Tk()
root.title("Monoalphabetic Cipher")
root.geometry("420x220")
root.configure(bg="#F0F8FF")

Label(root, text="Monoalphabetic Cipher", font=("Arial",16,"bold"),
      bg="#F0F8FF").grid(row=0, column=0, columnspan=2, pady=10)

Label(root, text="Message:", bg="#F0F8FF").grid(row=1,column=0,padx=10,pady=8)
msg = Entry(root, width=30)
msg.grid(row=1,column=1)

Button(root, text="Encrypt", bg="green", fg="white",
       command=lambda: run(True)).grid(row=2,column=0,pady=10)

Button(root, text="Decrypt", bg="blue", fg="white",
       command=lambda: run(False)).grid(row=2,column=1)

Label(root, text="Result:", bg="#F0F8FF").grid(row=3,column=0,pady=8)
out = Entry(root, width=30, state="readonly")
out.grid(row=3,column=1)

root.mainloop()


