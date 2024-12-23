import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from AppClass import*

cnt = 0

def OpenFile(window):

	#SELECTION OF A FILE
	name = window.filename = filedialog.askopenfilename(title = "Select a file", filetypes = [("text files", "*.txt")])
	NewWindow = tk.Toplevel(window)
	size = len(name) - 4
	cleanName = ""
	for i in range(size):
		if(name[size - i - 1] == '/'):
			break
		cleanName += name[size - 1 - i]
	cleanName = cleanName[::-1]

	#OPEN NEW WINDOW
	NewWindow.title(cleanName)
	NewWindow.geometry("300x200")


	#INTERPRET FROM FILE
	with open(name, "r") as file:
		line = file.readline()
		tk.Label(NewWindow, text = line).grid(row = 100, column = 100, padx = 20, pady = 20)

    #fali jos sve dalje za interpretirat
	expr = Formula(line)
	global cnt

	MinimizedLbl = tk.Label(NewWindow, text = "Minimized expression is: " + expr.sentence)
	MinimizeBtn = tk.Button(NewWindow, text = "Minimize expression", command = lambda: ShowMinimized(NewWindow, expr, MinimizedLbl))
	MinimizeBtn.grid(row = 200, column = 100, padx = 20, pady = 20)



    
def SaveFile():

	return

def SaveFileAs():
	return

def NewFile():
	return

def Help():
	messagebox.showinfo("Help", "Netriba ti pomoc osim ako si retard")

def About():
	messagebox.showinfo("About", "Project for OOP, made by Vatroslav Bočkaj Bundara\nversion 1.0.0")

def ShowMinimized(window, expr, lbl):
	global cnt
	cnt = (cnt + 1) % 2
	if cnt == 0:
		lbl.grid_forget()
	else:	
		lbl.grid(row = 300, column = 100, padx = 20, pady = 20)











