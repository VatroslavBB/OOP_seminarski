import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Table Example")

# Create a frame for the table
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Data for the table
columns = ("Name", "Age", "City")
data = [
    ("Alice", 25, "New York"),
    ("Bob", 30, "Los Angeles"),
    ("Charlie", 22, "Chicago"),
    ("Diana", 27, "San Francisco"),
    ("Alice", 25, "New York"),
    ("Bob", 30, "Los Angeles"),
    ("Charlie", 22, "Chicago"),
    ("Diana", 27, "San Francisco"),
    ("Alice", 25, "New York"),
    ("Bob", 30, "Los Angeles"),
    ("Charlie", 22, "Chicago"),
    ("Diana", 27, "San Francisco"),
    ("Alice", 25, "New York"),
    ("Bob", 30, "Los Angeles"),
    ("Charlie", 22, "Chicago"),
    ("Diana", 27, "San Francisco"),
    ("Alice", 25, "New York"),
    ("Bob", 30, "Los Angeles"),
    ("Charlie", 22, "Chicago"),
    ("Diana", 27, "San Francisco"),
    ("Alice", 25, "New York"),
    ("Bob", 30, "Los Angeles"),
    ("Charlie", 22, "Chicago"),
    ("Diana", 27, "San Francisco"),
    ("Alice", 25, "New York"),
    ("Bob", 30, "Los Angeles"),
    ("Charlie", 22, "Chicago"),
    ("Diana", 27, "San Francisco"),
    ("Alice", 25, "New York"),
    ("Bob", 30, "Los Angeles"),
    ("Charlie", 22, "Chicago"),
    ("Diana", 27, "San Francisco"),
    ("Alice", 25, "New York"),
    ("Bob", 30, "Los Angeles"),
    ("Charlie", 22, "Chicago"),
    ("Diana", 27, "San Francisco"),
    ("Alice", 25, "New York"),
    ("Bob", 30, "Los Angeles"),
    ("Charlie", 22, "Chicago"),
    ("Diana", 27, "San Francisco"),
    ("Alice", 25, "New York"),
    ("Bob", 30, "Los Angeles"),
    ("Charlie", 22, "Chicago"),
    ("Diana", 27, "San Francisco")
]

# Create the Treeview widget
tree = ttk.Treeview(frame, columns=columns, show='headings')

# Define the column headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor=tk.CENTER)

# Insert the data into the table
for row in data:
    tree.insert('', tk.END, values=row)

# Add a scrollbar
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Pack the Treeview widget
tree.pack(fill=tk.BOTH, expand=True)

# Start the Tkinter event loop
root.mainloop()
