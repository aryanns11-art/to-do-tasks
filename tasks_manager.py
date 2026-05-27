import tkinter as tk
from tkinter import messagebox
import os

FILE = "abcd.txt"

def load_tasks():
    if not os.path.exists(FILE):
        return[]
    with open(FILE,"r") as f :
        return[line.strip() for line in f.readlines()]
    
def save_tasks(tasks):
    with open(FILE,"w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_tasks():
    task = task_entry.get().strip()

    if not task:
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return

    if task in tasks:   
        messagebox.showwarning("Duplicate", "Task already exists!")
        return

    tasks.append(task)
    save_tasks(tasks)

    listbox.insert(tk.END, "✔ " + task)   
    task_entry.delete(0, tk.END)
    task_entry.focus()

def delete_tasks():
    try:
        selected = listbox.curselection()[0]

        deleted_task = tasks.pop(selected)   # get the actual task
        save_tasks(tasks)

        listbox.delete(selected)
        messagebox.showinfo("Deleted Task", f"Deleted: {deleted_task}")
    except:
        messagebox.showwarning("Warning", "Please select a task.")


def clear_all():
    
    comfirm=messagebox.askyesno("Confirm","Delete ALL tasks ?")
    if comfirm:
        tasks.clear()
        save_tasks(tasks)
        listbox.delete(0,tk.END)

root = tk.Tk()
root.title("To-Do List")        
root.geometry("450x550")
root.resizable(False,False)
root.config(bg="#f5f7fa")

title = tk.Label(
    root,
    text="📝 TO-DO LIST",
    font=("Segoe UI", 22, "bold"),
    bg="#f5f6fa",
    fg="#2d3436",
    padx=10,
    pady=10
)
title.pack(pady=10)

input_frame = tk.Frame(root, bg="#f5f7fa")  #Frame for input and add button
input_frame.pack(pady=10)

task_entry = tk.Entry(
    input_frame, 
    font=("Segoe UI", 12), 
    width=25, 
    relief="solid", 
    bd=1)
task_entry.bind("<Return>", lambda event: add_tasks())  # just press Enter instead of clicking button
task_entry.grid(row=0, column=0, padx=5, ipady=6)

add_btn = tk.Button(
    input_frame, 
    text="Add", 
    bg="#2ecc71", 
    fg="white", 
    width=8, 
    command=add_tasks)

add_btn.grid(row=0, column=1, padx=5)

list_frame = tk.Frame(root)
list_frame.pack(pady=15)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(
    list_frame,
    font=("Segoe UI", 12),
    width=35,
    height=15,
    bg="white",
    fg="#2c3e50",
    selectbackground="#a29bfe",
    activestyle="none",
    yscrollcommand=scrollbar.set       # When the list moves (scrolls), update the scrollbar position
)
listbox.pack()

scrollbar.config(command=listbox.yview)    # When scrollbar moves → scroll the list

btn_frame = tk.Frame(root, bg="#f5f7fa")
btn_frame.pack(pady=10)

delete_btn = tk.Button(
    btn_frame, 
    text="Delete", 
    width=10, 
    bg="#e74c3c", 
    fg="white", 
    command=delete_tasks)

delete_btn.grid(row=0, column=0, padx=5)

clear_btn = tk.Button(
    btn_frame, 
    text="Clear All", 
    width=10, 
    bg="#f39c12", 
    fg="white", 
    command=clear_all)

clear_btn.grid(row=0, column=1, padx=5)

exit_btn = tk.Button(
    btn_frame, 
    text="Exit", 
    width=10, 
    bg="#7f8c8d", 
    fg="white", 
    command=root.destroy)
exit_btn.grid(row=0, column=2, padx=5)

tasks = load_tasks()
for task in tasks:
    listbox.insert(tk.END, "✔ " + task)

root.mainloop()
