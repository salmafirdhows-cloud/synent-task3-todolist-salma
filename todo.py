import tkinter as tk
from tkinter import messagebox
import json

FILE_NAME = "tasks.json"

# ---------------- LOAD TASKS ----------------
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)

            for task in tasks:
                task_listbox.insert(tk.END, task)

    except FileNotFoundError:
        pass

# ---------------- SAVE TASKS ----------------
def save_tasks():
    tasks = task_listbox.get(0, tk.END)

    with open(FILE_NAME, "w") as file:
        json.dump(list(tasks), file)

# ---------------- ADD TASK ----------------
def add_task():
    task = task_entry.get()

    if task != "":
        formatted_task = f"🕒 {task}"

        task_listbox.insert(tk.END, formatted_task)

        task_entry.delete(0, tk.END)

        save_tasks()

    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# ---------------- DELETE TASK ----------------
def delete_task():
    try:
        selected_task = task_listbox.curselection()[0]

        task_listbox.delete(selected_task)

        save_tasks()

    except:
        messagebox.showwarning("Warning", "Please select a task!")

# ---------------- COMPLETE TASK ----------------
def complete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]

        selected_task = task_listbox.get(selected_task_index)

        if not selected_task.startswith("✅"):
            updated_task = selected_task.replace("🕒", "✅")

            task_listbox.delete(selected_task_index)

            task_listbox.insert(selected_task_index, updated_task)

            save_tasks()

    except:
        messagebox.showwarning("Warning", "Please select a task!")

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()

root.title("To-Do App")
root.geometry("650x650")
root.resizable(False, False)

# Pastel background
root.config(bg="#FFF6FB")

# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="📝 Salma's To-Do App 💅🏻",
    font=("Arial", 22, "bold"),
    bg="#FFF6FB",
    fg="#5E548E"
)

title.pack(pady=20)

# ---------------- INPUT ----------------
task_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 14),
    bg="#F7F1FF",
    fg="#5E548E",
    relief="flat",
    bd=5,
    insertbackground="#5E548E"
)

task_entry.pack(pady=10)

# ---------------- BUTTON FRAME ----------------
button_frame = tk.Frame(root, bg="#FFF6FB")

button_frame.pack(pady=10)

# ---------------- ADD BUTTON ----------------
add_button = tk.Button(
    button_frame,
    text="Add Task",
    font=("Arial", 12, "bold"),
    bg="#F8C8DC",
    fg="#5E548E",
    activebackground="#F4B6CF",
    activeforeground="#5E548E",
    padx=10,
    pady=5,
    relief="flat",
    command=add_task
)

add_button.grid(row=0, column=0, padx=10)

# ---------------- COMPLETE BUTTON ----------------
complete_button = tk.Button(
    button_frame,
    text="Complete",
    font=("Arial", 12, "bold"),
    bg="#C7F0DB",
    fg="#5E548E",
    activebackground="#B5EAD7",
    activeforeground="#5E548E",
    padx=10,
    pady=5,
    relief="flat",
    command=complete_task
)

complete_button.grid(row=0, column=1, padx=10)

# ---------------- DELETE BUTTON ----------------
delete_button = tk.Button(
    button_frame,
    text="Delete",
    font=("Arial", 12, "bold"),
    bg="#DCC6FF",
    fg="#5E548E",
    activebackground="#CDB4FF",
    activeforeground="#5E548E",
    padx=10,
    pady=5,
    relief="flat",
    command=delete_task
)

delete_button.grid(row=0, column=2, padx=10)

# ---------------- LIST FRAME ----------------
list_frame = tk.Frame(root, bg="#FFF6FB")

list_frame.pack(pady=20)

# ---------------- SCROLLBAR ----------------
scrollbar = tk.Scrollbar(list_frame)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# ---------------- TASK LIST ----------------
task_listbox = tk.Listbox(
    list_frame,
    width=50,
    height=15,
    font=("Arial", 12),
    bg="#F7F1FF",
    fg="#5E548E",
    selectbackground="#DCC6FF",
    selectforeground="#5E548E",
    relief="flat",
    bd=5,
    yscrollcommand=scrollbar.set
)

task_listbox.pack()

scrollbar.config(command=task_listbox.yview)

# ---------------- LOAD SAVED TASKS ----------------
load_tasks()

# ---------------- RUN APP ----------------
root.mainloop()
