import tkinter as tk
from tkinter import messagebox
import json
import os

# File to save tasks
TASKS_FILE = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Add task
def add_task():
    task = entry.get()
    if task != "":
        tasks.append({"task": task, "status": "Pending"})
        update_listbox()
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Delete task
def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        tasks.pop(selected_index)
        update_listbox()
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Mark as done
def mark_done():
    try:
        selected_index = listbox.curselection()[0]
        tasks[selected_index]["status"] = "Done"
        update_listbox()
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task!")

# Update display
def update_listbox():
    listbox.delete(0, tk.END)
    for t in tasks:
        listbox.insert(tk.END, f"{t['task']} - [{t['status']}]")

# Main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

tasks = load_tasks()

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)
tk.Button(root, text="Mark as Done", command=mark_done).pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

update_listbox()

root.mainloop()
