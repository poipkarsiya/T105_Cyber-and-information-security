import tkinter as tk
from tkinter import messagebox
from math import gcd

def prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

def inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d

def generate():
    global e, d, n
    try:
        p, q = int(ep.get()), int(eq.get())

        if not prime(p) or not prime(q):
            raise Exception("Enter prime numbers only.")
        if p == q:
            raise Exception("p and q must be different.")

        n = p * q
        if n <= 255:
            raise Exception("Choose larger prime numbers.")

        phi = (p - 1) * (q - 1)

        e = 3
        while gcd(e, phi) != 1:
            e += 2

        d = inverse(e, phi)

        pub.config(text=f"Public Key : ({e}, {n})")
        pri.config(text=f"Private Key : ({d}, {n})")

    except Exception as ex:
        messagebox.showerror("Error", ex)

def encrypt():
    try:
        cipher = [pow(ord(i), e, n) for i in msg.get()]
        txt.delete("1.0", tk.END)
        txt.insert(tk.END, str(cipher))
    except:
        messagebox.showerror("Error", "Generate Keys First.")

def decrypt():
    try:
        cipher = eval(txt.get("1.0", tk.END))
        result.config(text="Decrypted Message : " +
                      ''.join(chr(pow(i, d, n)) for i in cipher))
    except:
        messagebox.showerror("Error", "Invalid Cipher.")

root = tk.Tk()
root.title("RSA Encryption & Decryption")
root.geometry("500x500")
root.resizable(False, False)

tk.Label(root, text="RSA Encryption & Decryption",
         font=("Arial", 18, "bold")).pack(pady=15)

tk.Label(root, text="Prime Number (p)").pack()
ep = tk.Entry(root, width=40)
ep.pack()

tk.Label(root, text="Prime Number (q)").pack()
eq = tk.Entry(root, width=40)
eq.pack()

tk.Button(root, text="Generate Keys", width=20,
          bg="green", fg="white", command=generate).pack(pady=10)

pub = tk.Label(root, text="Public Key :", fg="blue")
pub.pack()

pri = tk.Label(root, text="Private Key :", fg="blue")
pri.pack()

tk.Label(root, text="Message").pack(pady=10)
msg = tk.Entry(root, width=40)
msg.pack()

tk.Button(root, text="Encrypt", width=20,
          bg="dodgerblue", fg="white", command=encrypt).pack(pady=10)

txt = tk.Text(root, width=40, height=5)
txt.pack()

tk.Button(root, text="Decrypt", width=20,
          bg="orange", fg="white", command=decrypt).pack(pady=10)

result = tk.Label(root, text="Decrypted Message :",
                  font=("Arial", 11, "bold"))
result.pack(pady=10)
root.mainloop()
