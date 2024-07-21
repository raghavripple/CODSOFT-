import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGen:
    def __init__(self, root):
        self.root = root
        self.root.title("PasswordGen")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.title_lbl = tk.Label(root, text="PasswordGen", font=("Helvetica", 18, "bold"))
        self.title_lbl.pack(pady=10)
        self.length_lbl = tk.Label(root, text="Enter the desired length for the password:")
        self.length_lbl.pack(pady=5)
        self.length_entry = tk.Entry(root, width=10)
        self.length_entry.pack(pady=5)
        self.include_upper = tk.BooleanVar()
        self.include_digits = tk.BooleanVar()
        self.include_special = tk.BooleanVar()
        self.upper_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.include_upper)
        self.upper_check.pack()
        self.digits_check = tk.Checkbutton(root, text="Include Digits", variable=self.include_digits)
        self.digits_check.pack()
        self.special_check = tk.Checkbutton(root, text="Include Special Characters", variable=self.include_special)
        self.special_check.pack()
        self.gen_btn = tk.Button(root, text="Generate Password", command=self.gen_password, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.gen_btn.pack(pady=10)
        self.result_lbl = tk.Label(root, text="", fg="blue", font=("Helvetica", 12))
        self.result_lbl.pack(pady=10)

    def gen_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Password length should be greater than 0.")
            chars = string.ascii_lowercase
            if self.include_upper.get():
                chars += string.ascii_uppercase
            if self.include_digits.get():
                chars += string.digits
            if self.include_special.get():
                chars += string.punctuation
            if not chars:
                raise ValueError("No character types selected!")
            password = ''.join(random.choice(chars) for _ in range(length))
            self.result_lbl.config(text=f"Generated Password: {password}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGen(root)
    root.mainloop()
