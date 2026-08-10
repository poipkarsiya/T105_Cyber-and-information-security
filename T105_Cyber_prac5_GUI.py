# ==========================================
# DIFFIE-HELLMAN KEY EXCHANGE - GUI
# ==========================================

import tkinter as tk
from tkinter import messagebox

def perform_diffie_hellman():
    try:
        p = int(entry_p.get())
        g = int(entry_g.get())
        siya = int(entry_siya.get())
        jay = int(entry_jay.get())

        if p <= 1 or g <= 0 or siya <= 0 or jay <= 0:
            messagebox.showerror("Invalid Input", "Please enter positive values.")
            return

        siya_public = pow(g, siya, p)
        jay_public = pow(g, jay, p)

        siya_key = pow(jay_public, siya, p)
        jay_key = pow(siya_public, jay, p)

        result_text.delete("1.0", tk.END)

        result_text.insert(
            tk.END,
            "========== SHARED SECRET KEY ==========\n\n"
            f"Siya's Shared Key: {siya_key}\n"
            f"Jay's Shared Key: {jay_key}\n\n"
        )

        if siya_key == jay_key:
            result_text.insert(
                tk.END,
                "✓ KEY EXCHANGE SUCCESSFUL\n"
                "✓ Both entities have the same shared secret key."
            )
        else:
            result_text.insert(
                tk.END,
                "✗ KEY EXCHANGE FAILED"
            )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid integer values."
        )

def clear_fields():
    entry_p.delete(0, tk.END)
    entry_g.delete(0, tk.END)
    entry_siya.delete(0, tk.END)
    entry_jay.delete(0, tk.END)
    result_text.delete("1.0", tk.END)

# Main Window
root = tk.Tk()
root.title("Diffie-Hellman Key Exchange")
root.geometry("700x700")
root.configure(bg="#f2f2f2")

tk.Label(
    root,
    text="DIFFIE-HELLMAN KEY EXCHANGE",
    font=("Arial", 20, "bold"),
    bg="#f2f2f2"
).pack(pady=20)

tk.Label(
    root,
    text="Secure Key Exchange over an Insecure Network",
    font=("Arial", 11),
    bg="#f2f2f2"
).pack(pady=5)

# Input Frame
input_frame = tk.Frame(
    root,
    bg="white",
    padx=25,
    pady=25
)

input_frame.pack(
    padx=40,
    pady=20,
    fill="x"
)

tk.Label(
    input_frame,
    text="PUBLIC PARAMETERS",
    font=("Arial", 13, "bold"),
    bg="white"
).grid(
    row=0,
    column=0,
    columnspan=2,
    pady=10
)

tk.Label(
    input_frame,
    text="Prime Number (p):",
    font=("Arial", 11),
    bg="white"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

entry_p = tk.Entry(
    input_frame,
    font=("Arial", 11),
    width=25
)

entry_p.grid(
    row=1,
    column=1,
    padx=10,
    pady=8
)

tk.Label(
    input_frame,
    text="Primitive Root (g):",
    font=("Arial", 11),
    bg="white"
).grid(
    row=2,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

entry_g = tk.Entry(
    input_frame,
    font=("Arial", 11),
    width=25
)

entry_g.grid(
    row=2,
    column=1,
    padx=10,
    pady=8
)

tk.Label(
    input_frame,
    text="PRIVATE KEYS",
    font=("Arial", 13, "bold"),
    bg="white"
).grid(
    row=3,
    column=0,
    columnspan=2,
    pady=15
)

tk.Label(
    input_frame,
    text="Siya Private Key:",
    font=("Arial", 11),
    bg="white"
).grid(
    row=4,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

entry_siya = tk.Entry(
    input_frame,
    font=("Arial", 11),
    width=25
)

entry_siya.grid(
    row=4,
    column=1,
    padx=10,
    pady=8
)

tk.Label(
    input_frame,
    text="Jay Private Key:",
    font=("Arial", 11),
    bg="white"
).grid(
    row=5,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)

entry_jay = tk.Entry(
    input_frame,
    font=("Arial", 11),
    width=25
)

entry_jay.grid(
    row=5,
    column=1,
    padx=10,
    pady=8
)

# Buttons
button_frame = tk.Frame(
    root,
    bg="#f2f2f2"
)

button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Generate Shared Key",
    font=("Arial", 11, "bold"),
    command=perform_diffie_hellman,
    padx=15,
    pady=8
).grid(
    row=0,
    column=0,
    padx=10
)

tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 11, "bold"),
    command=clear_fields,
    padx=20,
    pady=8
).grid(
    row=0,
    column=1,
    padx=10
)

# Result
tk.Label(
    root,
    text="RESULT",
    font=("Arial", 13, "bold"),
    bg="#f2f2f2"
).pack(pady=10)


result_text = tk.Text(
    root,
    height=10,
    width=75,
    font=("Courier New", 11),
    padx=10,
    pady=10
)

result_text.pack(
    padx=30,
    pady=10
)

root.mainloop()
