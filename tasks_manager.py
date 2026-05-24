import tkinter as tk
from tkinter import messagebox
import os

FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

# Save tasks to file
def save_tasks(tasks):
    with open(FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Add task
def add_task():
    task = task_entry.get()

    if task != "":
        tasks.append(task)
        save_tasks(tasks)

        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Delete selected task
def delete_task():
    try:
        selected = listbox.curselection()[0]

        removed = tasks.pop(selected)
        save_tasks(tasks)

        listbox.delete(selected)

        messagebox.showinfo("Deleted", f"Deleted: {removed}")

    except:
        messagebox.showwarning("Warning", "Please select a task.")

# Load existing tasks
tasks = load_tasks()

# Main window
root = tk.Tk()
root.title("To-Do List") 
root.geometry("400x500")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="TO-DO LIST",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

# Entry box
task_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=25
)
task_entry.pack(pady=10)

# Add button
add_button = tk.Button(
    root,
    text="Add Task",
    font=("Arial", 12),
    width=15,
    command=add_task
)
add_button.pack(pady=5)

# Task list
listbox = tk.Listbox(
    root,
    font=("Arial", 14),
    width=35,
    height=12
)
listbox.pack(pady=10)

# Insert saved tasks into listbox
for task in tasks:
    listbox.insert(tk.END, task)

# Delete button
delete_button = tk.Button(
    root,
    text="Delete Task",
    font=("Arial", 12),
    width=15,
    command=delete_task
)
delete_button.pack(pady=5)

# Exit button
exit_button = tk.Button(
    root,
    text="Exit",
    font=("Arial", 12),
    width=15,
    command=root.destroy
)
exit_button.pack(pady=10)

# Run app
root.mainloop()