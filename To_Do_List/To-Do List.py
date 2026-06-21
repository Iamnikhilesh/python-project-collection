# TO-DO-LIST
import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        # Entry widget for task input
        self.task_entry = tk.Entry(self.master, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Button to add task
        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Listbox to display tasks
        self.tasks_listbox = tk.Listbox(self.master, width=50, height=10)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Button to delete selected task
        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=10, pady=10)

        # Button to clear all tasks
        self.clear_button = tk.Button(self.master, text="Clear All", command=self.clear_tasks)
        self.clear_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.tasks_listbox.insert(tk.END, task_text)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.tasks_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def clear_tasks(self):
        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
        if confirmed:
            self.tasks = []
            self.tasks_listbox.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
