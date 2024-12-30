
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from AppClass import*

MinimizedUsed = False
TruthTableUsed = False

function = Formula("a", "a")


def ResetGlobals():
	global MinimizedUsed, TruthTableUsed

	TruthTableUsed = False
	MinimizedUsed = False

def BackToBeginning(window, frame1, frame2):
	frame1.destroy()
	frame2.destroy()

	ResetGlobals()

	frame1 = tk.Frame(window, bd = 1, relief = "sunken")
	choice = tk.IntVar(value = -1)

	ManualBtn = tk.Radiobutton(frame1, text = "Manualan unos", value = -1, variable = choice)
	FromFileBtn = tk.Radiobutton(frame1, text = "Unos iz datoteke", value = 1, variable = choice)
	EnterBtn = tk.Button(frame1, text = "Zaključaj odabir", command = lambda: InputMethod(choice.get(), window, frame1))

	ManualBtn.pack(anchor = "center", padx = 20, pady = 10)
	FromFileBtn.pack(anchor = "center", padx = 20, pady = 10)
	EnterBtn.pack(anchor = "center", padx = 20, pady = 20)
	frame1.pack(side = "left", fill = "y")


def Clear(frame, remain = []):
	ResetGlobals()

	for widget in frame.winfo_children():
		inside = False
		for i in range(len(remain)):
			if widget == remain[i]:
				inside = True
				break
		if inside == False:
			widget.destroy()


def MaximizeWindow(window):
	window.attributes("-fullscreen", True)

def MinimizeWindow(window):
	window.attributes("-fullscreen", False)
	window.geometry("300x400")

def ShowMinimized(frame, expr):
	global MinimizedUsed
	MinimizedLbl = tk.Label(frame, text = "Minimizirana funkcija: " + expr.minimal)
	if MinimizedUsed == True:
		return
	else:
		MinimizedUsed = True
		MinimizedLbl.pack(anchor = "w", padx = 20, pady = 20)
		return


def ShowTruthTable(expr, frame):
	global TruthTableUsed

	table = ttk.Treeview(frame, columns = expr.truthtable[0], show = "headings", height = len(expr.truthtable))

	if TruthTableUsed == True:
		return
	else:
		TruthTableUsed = True

		for heading in expr.truthtable[0]:
			table.heading(heading, text = heading)
			table.column(heading, width = 40, anchor = "center")

		for row in expr.truthtable[1:]:
			table.insert('', "end", values = row)

		table.pack(fill = "both")
		return


def ShowVeitchDiagram(expr, frame):
	return


def EnterFunction(FuncEntry, VarsEntry, frame):
	global function

	function = Formula(FuncEntry.get(), VarsEntry.get())

	if function.CheckVars() == False:
		messagebox.showerror("Krivo", "Varijable je nemoguce procitati")
	elif function.valid == False:
		messagebox.showerror("Krivo", "Recenica nije sintakticki ispravna")
	else:
		return


def InputMethod(c, window, frame):
	if c == 1:
		OpenFile(window, frame)
	else:
		ManualInput(window, frame)

def ManualInput(window, frame):
	global function

	Clear(frame)

	CalcFrame = tk.Frame(window, bd = 1, relief = "sunken")
	CalcFrame.pack(side = "left", fill = "both", expand = True)

	FunctionLbl = tk.Label(CalcFrame, text = "Booleova funkcija u fileu je\nf( ) = ")

	VarsLbl = tk.Label(CalcFrame, text = "Ovdje unesite varijable (min. 1, max. 5), dopustena su samo velika i mala slova")
	FuncLbl = tk.Label(CalcFrame, text = "Ovdje unesite booleovu funkciju\n - negacija '!'\n konjunkcija '&'\n disjunkcija '|'\npisite sve skupa")

	FunctionEntry = tk.Entry(CalcFrame, width = 40, relief = "sunken")
	VarsEntry = tk.Entry(CalcFrame, width = 15, relief = "sunken")
	VarsLbl.pack(anchor = "center", padx = 20, pady = 5)
	VarsEntry.pack(anchor = "center", padx = 20, pady = 5)
	FuncLbl.pack(anchor = "center", padx = 20, pady = 5)
	FunctionEntry.pack(anchor = "center", padx = 20, pady = 5)

	EnterFunctionBtn = tk.Button(frame, text = "Unesi", command = lambda: EnterFunction(FunctionEntry, VarsEntry, CalcFrame))
	MinimizeBtn = tk.Button(frame, text = "Minimizirana funkcija", command  = lambda: ShowMinimized(CalcFrame, function))
	ShowTruthBtn = tk.Button(frame, text = "Tablica istine", command = lambda: ShowTruthTable(function, CalcFrame))
	ShowVeitchBtn = tk.Button(frame, text = "Veitchev diagram")
	ClearBtn = tk.Button(frame, text = "Brisanje", command = lambda: Clear(CalcFrame, remain = [FunctionLbl, FunctionEntry, VarsEntry, VarsLbl, FuncLbl]))
	SaveBtn = tk.Button(frame, text = "Spremi")
	SaveAsBtn = tk.Button(frame, text = "Spremi kao")
	BackBtn = tk.Button(frame, text = "Natrag", command = lambda: BackToBeginning(window, frame, CalcFrame))

	EnterFunctionBtn.pack(anchor = "w", padx = 20, pady = 20)
	MinimizeBtn.pack(anchor = "w", padx = 20, pady = 20)
	ShowTruthBtn.pack(anchor = "w", padx = 20, pady = 20)
	ShowVeitchBtn.pack(anchor = "w", padx = 20, pady = 20)
	ClearBtn.pack(anchor = "w", padx = 20, pady = 20)
	FunctionLbl.pack(anchor = "center", padx = 20, pady = 20)
	BackBtn.pack(anchor = "w", padx = 20, pady = 20)
	SaveBtn.pack(anchor = "w", padx = 20, pady = 20)
	SaveAsBtn.pack(anchor = "w", padx = 20, pady = 20)


def OpenFile(window, frame):
	#brisi toolbar
	Clear(frame)

	CalcFrame = tk.Frame(window, bd = 1, relief = "sunken")
	CalcFrame.pack(side = "left", fill = "both", expand = True)

	#biraj file
	name = filedialog.askopenfilename(title = "Odaberite tekstualnu datoteku", filetypes = [("text files", "*.txt")])
	print(name)

	if name == "":
		return BackToBeginning(window, frame, CalcFrame)


	#procitaj file
	with open(name, "r") as file:
		variables = file.readline()
		function = file.readline()


	expr = Formula(function, variables[:-1])

	FunctionLbl = tk.Label(CalcFrame, text = "Booleova funkcija u fileu je\nf(" + expr.variables + ") = " + expr.sentence)

	MinimizeBtn = tk.Button(frame, text = "Minimizirana funkcija", command = lambda: ShowMinimized(CalcFrame, expr))
	ShowTruthBtn = tk.Button(frame, text = "Tablica istine", command = lambda: ShowTruthTable(expr, CalcFrame))
	ShowVeitchBtn = tk.Button(frame, text = "Veitchev diagram", command = lambda: ShowVeitchDiagram(expr, CalcFrame))
	ClearBtn = tk.Button(frame, text = "Brisanje", command = lambda: Clear(CalcFrame, remain = [FunctionLbl]))
	BackBtn = tk.Button(frame, text = "Natrag", command = lambda: BackToBeginning(window, frame, CalcFrame))

	MinimizeBtn.pack(anchor = "w", padx = 20, pady = 20)
	ShowTruthBtn.pack(anchor = "w", padx = 20, pady = 20)
	ShowVeitchBtn.pack(anchor = "w", padx = 20, pady = 20)
	ClearBtn.pack(anchor = "w", padx = 20, pady = 20)
	FunctionLbl.pack(anchor = "center", padx = 20, pady = 20)
	BackBtn.pack(anchor = "w", padx = 20, pady = 20)

def Help():
	messagebox.showinfo("Help", "Stisci botune pas vidit")

def About():
	messagebox.showinfo("About", "Seminarski rad iz kolegija OOP\nnapravio Vatroslav Bočkaj Bundara\nversion 1.0.0")


def CreateMenuBar(window, file = False, exit = False, win = False, info = False):
	NewMenuBar = tk.Menu(window)
	window.config(menu = NewMenuBar)

	#file
	if file == True:
		FileMenu = tk.Menu(NewMenuBar, tearoff = 0)
		FileMenu.add_command(label = "Save", command = lambda: SaveFile())
		FileMenu.add_command(label = "Save as", command = lambda: SaveFileAs())
		NewMenuBar.add_cascade(label = "File", menu = FileMenu)

	#exit
	if exit == True:
		ExitMenu = tk.Menu(NewMenuBar, tearoff = 0)
		ExitMenu.add_command(label = "Exit", command = window.destroy)
		NewMenuBar.add_cascade(label = "Exit", menu = ExitMenu)

	#info
	if info == True:
		InfoMenu = tk.Menu(NewMenuBar, tearoff = 0)
		InfoMenu.add_command(label = "Help", command = Help)
		InfoMenu.add_command(label = "About", command = About)
		NewMenuBar.add_cascade(label = "Info", menu = InfoMenu)

	#window
	if win == True:
		WindowMenu = tk.Menu(NewMenuBar, tearoff = 0)
		WindowMenu.add_command(label = "Minimize", command = lambda: MinimizeWindow(window))
		WindowMenu.add_command(label = "Maximize", command = lambda: MaximizeWindow(window))
		NewMenuBar.add_cascade(label = "Window", menu = WindowMenu)

























