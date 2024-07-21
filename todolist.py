
import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDoList")
        self.tasks = []
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        self.entry = tk.Entry(self.frame, width=40)
        self.entry.pack(side=tk.LEFT, padx=10)
        self.addbtn = tk.Button(self.frame, text="AddTask", command=self.add_task)
        self.addbtn.pack(side=tk.LEFT)
        self.listbox = tk.Listbox(self.root, width=50, height=15)
        self.listbox.pack(pady=20)
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.taskmenu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Tasks", menu=self.taskmenu)
        self.taskmenu.add_command(label="DeleteTask", command=self.delete_task)
        self.taskmenu.add_command(label="MarkDone", command=self.mark_done)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append({"task": task, "status": "Pending"})
            self.update_listbox()
            self.entry.delete(0, tk.END)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks):
            taskstr = f"{idx}. {task['task']} - {task['status']}"
            self.listbox.insert(tk.END, taskstr)

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            del self.tasks[selected[0]]
            self.update_listbox()

    def mark_done(self):
        selected = self.listbox.curselection()
        if selected:
            self.tasks[selected[0]]["status"] = "Done"
            self.update_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
