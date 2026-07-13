#1 Rail Fence Cipher CLI
def encrypt(text, key):
    rail = [''] * key
    row, step = 0, 1

    for ch in text:
        rail[row] += ch
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    return ''.join(rail)

def decrypt(cipher, key):
    mark = [[''] * len(cipher) for _ in range(key)]

    row, step = 0, 1
    for i in range(len(cipher)):
        mark[row][i] = '*'
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    k = 0
    for i in range(key):
        for j in range(len(cipher)):
            if mark[i][j] == '*':
                mark[i][j] = cipher[k]
                k += 1

    result = ""
    row, step = 0, 1
    for i in range(len(cipher)):
        result += mark[row][i]
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    return result

while True:
    print("\nRail Fence Cipher")
    print("1. Encrypt\n2. Decrypt\n3. Exit")

    ch = input("Choice: ")

    if ch == "1":
        print("Cipher:", encrypt(input("Enter Message: "), int(input("Enter Key: "))))

    elif ch == "2":
        print("Plain:", decrypt(input("Enter Cipher: "), int(input("Enter Key: "))))

    elif ch == "3":
        break

    else:
        print("Invalid Choice")



#2 Columnar Transposition Cipher CLI
import math

def encrypt(text, key):
    return ''.join(text[i::key] for i in range(key))

def decrypt(text, key):
    cols = math.ceil(len(text) / key)
    rows = key
    shade = cols * rows - len(text)
    plain = [''] * cols
    c = r = 0

    for ch in text:
        plain[c] += ch
        c += 1
        if c == cols or (c == cols - 1 and r >= rows - shade):
            c = 0
            r += 1

    return ''.join(plain)

while True:
    print("\nColumnar Transposition")
    print("1. Encrypt\n2. Decrypt\n3. Exit")

    ch = input("Choice: ")

    if ch == "1":
        print("Cipher:", encrypt(input("Enter Message: "), int(input("Enter Key: "))))

    elif ch == "2":
        print("Plain:", decrypt(input("Enter Cipher: "), int(input("Enter Key: "))))

    elif ch == "3":
        break

    else:
        print("Invalid Choice")




#1 Rail Fence Cipher GUI
from tkinter import *

def cipher(enc):
    text = msg.get()
    key = int(k.get())

    if enc:
        rail = [''] * key
        r, s = 0, 1
        for c in text:
            rail[r] += c
            if r == 0: s = 1
            elif r == key-1: s = -1
            r += s
        ans = ''.join(rail)

    else:
        n = len(text)
        arr = [['']*n for _ in range(key)]
        r, s = 0, 1

        for i in range(n):
            arr[r][i] = '*'
            if r == 0: s = 1
            elif r == key-1: s = -1
            r += s

        x = 0
        for i in range(key):
            for j in range(n):
                if arr[i][j] == '*':
                    arr[i][j] = text[x]
                    x += 1

        ans = ''
        r, s = 0, 1
        for i in range(n):
            ans += arr[r][i]
            if r == 0: s = 1
            elif r == key-1: s = -1
            r += s

    out.config(state="normal")
    out.delete(0, END)
    out.insert(0, ans)
    out.config(state="readonly")


root = Tk()
root.title("Rail Fence Cipher")
root.geometry("420x230")
root.configure(bg="#EAF4FC")
root.resizable(False, False)

Label(root,text="Rail Fence Cipher",
      font=("Arial",16,"bold"),
      bg="#EAF4FC").grid(row=0,column=0,columnspan=2,pady=10)

Label(root,text="Message:",bg="#EAF4FC").grid(row=1,column=0,padx=10,pady=8)
msg=Entry(root,width=30)
msg.grid(row=1,column=1)

Label(root,text="Key:",bg="#EAF4FC").grid(row=2,column=0,padx=10)
k=Entry(root,width=10)
k.grid(row=2,column=1,sticky="w")

Button(root,text="Encrypt",bg="green",fg="white",
       command=lambda:cipher(True)).grid(row=3,column=0,pady=15)

Button(root,text="Decrypt",bg="blue",fg="white",
       command=lambda:cipher(False)).grid(row=3,column=1)

Label(root,text="Result:",bg="#EAF4FC").grid(row=4,column=0)
out=Entry(root,width=30,state="readonly")
out.grid(row=4,column=1)

root.mainloop()



#2 Columnar Transposition Cipher GUI
from tkinter import *
import math

def encrypt(text, key):
    return ''.join(text[i::key] for i in range(key))

def decrypt(text, key):
    cols = math.ceil(len(text) / key)
    rows = key
    shade = cols * rows - len(text)
    plain = [''] * cols
    c = r = 0

    for ch in text:
        plain[c] += ch
        c += 1
        if c == cols or (c == cols - 1 and r >= rows - shade):
            c = 0
            r += 1
    return ''.join(plain)

def run(mode):
    text = msg.get()
    key = int(k.get())

    ans = encrypt(text, key) if mode == "E" else decrypt(text, key)

    out.config(state="normal")
    out.delete(0, END)
    out.insert(0, ans)
    out.config(state="readonly")

root = Tk()
root.title("Transposition Cipher")
root.geometry("430x220")
root.configure(bg="#F0F8FF")
root.resizable(False, False)

Label(root, text="Transposition Cipher",
      font=("Arial", 16, "bold"),
      bg="#F0F8FF", fg="navy").grid(row=0, column=0, columnspan=2, pady=10)

Label(root, text="Message:", bg="#F0F8FF",
      font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=8, sticky="e")
msg = Entry(root, width=30, font=("Arial", 11))
msg.grid(row=1, column=1)

Label(root, text="Key:", bg="#F0F8FF",
      font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=8, sticky="e")
k = Entry(root, width=10, font=("Arial", 11))
k.grid(row=2, column=1, sticky="w")

Button(root, text="Encrypt", bg="#4CAF50", fg="white",
       width=12, command=lambda: run("E")).grid(row=3, column=0, pady=15)

Button(root, text="Decrypt", bg="#2196F3", fg="white",
       width=12, command=lambda: run("D")).grid(row=3, column=1)

Label(root, text="Result:", bg="#F0F8FF",
      font=("Arial", 11)).grid(row=4, column=0, padx=10, sticky="e")
out = Entry(root, width=30, font=("Arial", 11), state="readonly")
out.grid(row=4, column=1)

root.mainloop()


