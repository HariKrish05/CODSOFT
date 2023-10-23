import tkinter as tk
from tkinter import messagebox

# Function to add a new task to the to-do list
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Pleas type a task to Enter!")

# Function to delete a selected task from the to-do list
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Create the main window
window = tk.Tk()
window.title("To-Do manager")

# Create entry for task input
entry = tk.Entry(window, width=40)
entry.pack(padx=10, pady=10)

# Create buttons for adding and deleting tasks
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(padx=10, pady=5)
delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(padx=10, pady=5)

# Create listbox to display tasks
listbox = tk.Listbox(window, width=50)
listbox.pack(padx=10, pady=10)

# Start the GUI
window.mainloop()