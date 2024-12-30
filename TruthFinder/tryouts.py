
import tkinter as tk

# Parameters
rows = 5
cols = 5
circle_rows = [1, 3]  # Rows to circle (0-indexed)
circle_cols = [2, 4]  # Columns to circle (0-indexed)
cell_width = 50
cell_height = 50

def draw_table(canvas, rows, cols, cell_width, cell_height):
    """Draws a table with the specified number of rows and columns."""
    for r in range(rows):
        for c in range(cols):
            x1 = c * cell_width
            y1 = r * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            # Draw cell rectangle
            canvas.create_rectangle(x1, y1, x2, y2, outline="black")
            # Add text to the cell
            canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=f"{r},{c}")

def draw_circles(canvas, circle_rows, circle_cols, cell_width, cell_height):
    """Draws circles around the specified rows and columns."""
    for r in circle_rows:
        for c in circle_cols:
            x = c * cell_width + cell_width / 2
            y = r * cell_height + cell_height / 2
            radius = min(cell_width, cell_height) / 2 - 5
            canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline="red", width=2)

# Create the main Tkinter window
root = tk.Tk()
root.title("Tkinter Table with Circles")

# Create a Canvas widget
canvas = tk.Canvas(root, width=cols * cell_width, height=rows * cell_height, bg="white")
canvas.pack()

# Draw the table
draw_table(canvas, rows, cols, cell_width, cell_height)

# Draw the circles
draw_circles(canvas, circle_rows, circle_cols, cell_width, cell_height)

# Run the Tkinter main loop
root.mainloop()


