#GUI
import tkinter as tk
from tkinter import messagebox
import hmac, hashlib

def generate():
    k, m = key.get(), msg.get()

    if not k or not m:
        messagebox.showwarning("Warning", "Enter Key and Message")
        return

    mac.delete(0, tk.END)
    mac.insert(0, hmac.new(
        k.encode(), m.encode(), hashlib.sha256
    ).hexdigest())

    status.config(text="✓ MAC Generated Successfully", fg="#16803c")

def verify():
    k, m, x = key.get(), msg.get(), mac.get().strip()

    if not k or not m or not x:
        messagebox.showwarning(
            "Warning", "Enter Key, Message and MAC"
        )
        return

    y = hmac.new(
        k.encode(), m.encode(), hashlib.sha256
    ).hexdigest()

    if hmac.compare_digest(x, y):
        status.config(
            text="✓ MAC VERIFIED — Message is Authentic",
            fg="#16803c"
        )
    else:
        status.config(
            text="✗ MAC VERIFICATION FAILED",
            fg="#d62828"
        )

def clear():
    key.delete(0, tk.END)
    msg.delete(0, tk.END)
    mac.delete(0, tk.END)
    status.config(text="")

root = tk.Tk()
root.title("Message Authentication Code")
root.geometry("720x570")
root.configure(bg="#eef2f7")
root.resizable(False, False)

# Header
head = tk.Frame(root, bg="#1e3a5f", height=90)
head.pack(fill="x")

tk.Label(
    head, text="MESSAGE AUTHENTICATION CODE",
    font=("Arial", 21, "bold"),
    fg="white", bg="#1e3a5f"
).pack(pady=(20, 3))

tk.Label(
    head, text="HMAC • SHA-256",
    font=("Arial", 10),
    fg="#dbeafe", bg="#1e3a5f"
).pack()

# Main Card
card = tk.Frame(root, bg="white", padx=35, pady=25)
card.pack(padx=45, pady=30, fill="x")

def field(name, show=""):
    tk.Label(
        card, text=name,
        font=("Arial", 11, "bold"),
        bg="white", fg="#1f2937"
    ).pack(anchor="w", pady=(5, 5))

    e = tk.Entry(
        card, font=("Arial", 12),
        width=65, show=show,
        relief="solid", bd=1
    )
    e.pack(ipady=7, pady=(0, 15))
    return e

key = field("Secret Key", "*")
msg = field("Message")
mac = field("Generated / Received MAC")

# Buttons
buttons = tk.Frame(card, bg="white")
buttons.pack(pady=5)

def button(text, command, color, width):
    tk.Button(
        buttons, text=text,
        command=command,
        width=width,
        font=("Arial", 10, "bold"),
        bg=color, fg="white",
        activeforeground="white",
        relief="flat",
        cursor="hand2"
    ).pack(side="left", padx=6, ipady=7)

button("GENERATE MAC", generate, "#2563eb", 18)
button("VERIFY MAC", verify, "#16a34a", 18)
button("CLEAR", clear, "#6b7280", 12)

# Status INSIDE card
status = tk.Label(
    card,
    text="",
    font=("Arial", 12, "bold"),
    bg="white"
)
status.pack(pady=(18, 0))

# Footer
tk.Label(
    root,
    text="Ensures Data Integrity and Authenticity",
    font=("Arial", 9),
    fg="#6b7280",
    bg="#eef2f7"
).pack()

root.mainloop()
