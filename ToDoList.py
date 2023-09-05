import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        tasks.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task_index = tasks.curselection()
    if selected_task_index:
        tasks.delete(selected_task_index)

def mark_as_done():
    selected_task_index = tasks.curselection()
    if selected_task_index:
        task_text = tasks.get(selected_task_index)
        tasks.delete(selected_task_index)
        completed_tasks.insert(tk.END, task_text)

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x700")

# Create and place GUI elements
entry = tk.Entry(root)
entry.pack(padx=10, pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

mark_done_button = tk.Button(root, text="Mark as Done", command=mark_as_done)
mark_done_button.pack()

tasks = tk.Listbox(root)
tasks.pack(padx=10, pady=10)

completed_tasks = tk.Listbox(root)
completed_tasks.pack(padx=10, pady=10)

# Start the main loop
root.mainloop()

