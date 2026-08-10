import tkinter as tk
from tkinter import messagebox
import hashlib

# RSA Functions
def generate_keys():
    p, q = 61, 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def get_hash(message):
    return int(hashlib.sha256(message.encode()).hexdigest(), 16)

def create_signature(message, key):
    d, n = key
    return pow(get_hash(message), d, n)

def verify_signature(message, signature, key):
    e, n = key
    return pow(signature, e, n) == get_hash(message) % n


# Variables
public_key = private_key = signature = None


# GUI Functions
def generate_key_button():
    global public_key, private_key

    public_key, private_key = generate_keys()

    public_key_box.delete("1.0", tk.END)
    private_key_box.delete("1.0", tk.END)

    public_key_box.insert(tk.END, str(public_key))
    private_key_box.insert(tk.END, str(private_key))

    result_label.config(
        text="RSA Keys Generated Successfully!", fg="green")


def sign_message():
    global signature

    if public_key is None:
        messagebox.showwarning("Warning", "Please generate RSA keys first.")
        return

    message = message_box.get("1.0", tk.END).strip()

    if not message:
        messagebox.showwarning("Warning", "Please enter a message.")
        return

    signature = create_signature(message, private_key)

    signature_box.delete("1.0", tk.END)
    signature_box.insert(tk.END, str(signature))

    result_label.config(
        text="Message Signed Successfully!", fg="blue")


def verify_message():
    if public_key is None:
        messagebox.showwarning("Warning", "Please generate RSA keys first.")
        return

    if signature is None:
        messagebox.showwarning("Warning", "Please sign the message first.")
        return

    message = message_box.get("1.0", tk.END).strip()

    if not message:
        messagebox.showwarning("Warning", "Please enter a message.")
        return

    if verify_signature(message, signature, public_key):
        result_label.config(
            text="✓ SIGNATURE VERIFIED\nMessage is Authentic and Unmodified",
            fg="green")
    else:
        result_label.config(
            text="✗ VERIFICATION FAILED\nMessage has been Modified!",
            fg="red")


def clear_all():
    global public_key, private_key, signature

    public_key = private_key = signature = None

    for box in [message_box, public_key_box,
                private_key_box, signature_box]:
        box.delete("1.0", tk.END)

    result_label.config(
        text="Enter a message and generate RSA keys", fg="black")


# Main Window
root = tk.Tk()
root.title("RSA Digital Signature")
root.geometry("750x700")
root.resizable(False, False)
root.configure(bg="#f2f4f7")


# Title
tk.Label(
    root, text="RSA DIGITAL SIGNATURE",
    font=("Arial", 24, "bold"),
    bg="#263238", fg="white", pady=15
).pack(fill="x")

tk.Label(
    root, text="Digital Signature Generation & Verification",
    font=("Arial", 12), bg="#f2f4f7", fg="#555555"
).pack(pady=10)


# Message
tk.Label(
    root, text="Enter Message",
    font=("Arial", 12, "bold"),
    bg="#f2f4f7"
).pack(anchor="w", padx=40)

message_box = tk.Text(
    root, height=4, width=75,
    font=("Arial", 11), relief="solid"
)
message_box.pack(padx=40, pady=5)


# Buttons
button_frame = tk.Frame(root, bg="#f2f4f7")
button_frame.pack(pady=10)

buttons = [
    ("Generate RSA Keys", generate_key_button, "#1976D2"),
    ("Sign Message", sign_message, "#388E3C"),
    ("Verify Signature", verify_message, "#F57C00")
]

for i, (text, command, color) in enumerate(buttons):
    tk.Button(
        button_frame, text=text, command=command,
        font=("Arial", 11, "bold"),
        bg=color, fg="white", width=18, pady=8
    ).grid(row=0, column=i, padx=5)


# Keys
key_frame = tk.Frame(root, bg="#f2f4f7")
key_frame.pack(pady=5)

tk.Label(
    key_frame, text="Public Key",
    font=("Arial", 10, "bold"), bg="#f2f4f7"
).grid(row=0, column=0, sticky="w")

tk.Label(
    key_frame, text="Private Key",
    font=("Arial", 10, "bold"), bg="#f2f4f7"
).grid(row=0, column=1, sticky="w")

public_key_box = tk.Text(key_frame, height=2, width=32)
public_key_box.grid(row=1, column=0, padx=5)

private_key_box = tk.Text(key_frame, height=2, width=32)
private_key_box.grid(row=1, column=1, padx=5)


# Digital Signature
tk.Label(
    root, text="Digital Signature",
    font=("Arial", 11, "bold"), bg="#f2f4f7"
).pack(anchor="w", padx=40, pady=(10, 2))

signature_box = tk.Text(
    root, height=3, width=75,
    font=("Arial", 10), relief="solid"
)
signature_box.pack(padx=40)


# Result
result_label = tk.Label(
    root,
    text="Enter a message and generate RSA keys",
    font=("Arial", 13, "bold"),
    bg="#f2f4f7", pady=15
)
result_label.pack()


# Clear Button
tk.Button(
    root, text="Clear All", command=clear_all,
    font=("Arial", 11, "bold"),
    bg="#D32F2F", fg="white",
    width=15, pady=7
).pack(pady=5)


# Footer
tk.Label(
    root, text="Practical 4 • RSA Digital Signature",
    font=("Arial", 9), bg="#f2f4f7", fg="#777777"
).pack(side="bottom", pady=10)

root.mainloop()
