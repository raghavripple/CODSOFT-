import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expr = ""
        self.input_text = tk.StringVar()
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()
        self.input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=('Arial', 18), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()
        self.add_buttons()

    def add_buttons(self):
        buttons = ['7', '8', '9', '/', 'C', '4', '5', '6', '*', '(', '1', '2', '3', '-', ')', '0', '.', '=', '+', 'DEL']
        row = 0
        col = 0
        for btn in buttons:
            if btn == "=":
                tk.Button(self.button_frame, text=btn, height=3, width=7, command=self.evaluate).grid(row=row, column=col, columnspan=2)
                col += 1
            else:
                tk.Button(self.button_frame, text=btn, height=3, width=7, command=lambda b=btn: self.on_button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 4:
                col = 0
                row += 1

    def on_button_click(self, char):
        if char == "C":
            self.expr = ""
        elif char == "DEL":
            self.expr = self.expr[:-1]
        else:
            self.expr += str(char)
        self.input_text.set(self.expr)

    def evaluate(self):
        try:
            result = str(eval(self.expr))
            self.input_text.set(result)
            self.expr = result
        except:
            messagebox.showerror("Error", "Invalid Expression")
            self.expr = ""
            self.input_text.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
