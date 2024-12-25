
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from AppClass import*

cnt = 0
entryCnt = 0
TTCnt = 0


def BackToBeginning(window, frame1, frame2):
	frame1.destroy()
	frame2.destroy()

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
	for widget in frame.winfo_children():
		inside = False
		for i in range(len(remain)):
			if widget == remain[i]:
				inside = True
				break
		if inside == False:
			widget.destroy()

def ShowTruthTable(expr, frame):
	global TTCnt
	TTCnt = (TTCnt + 1) % 2

	TT = ""

	for R in expr.truthtable:
		print(*R)
		TT += str(R) + "\n"


	TruthTableLbl = tk.Label(frame, text = TT)

	if TTCnt == 0:
		TruthTableLbl.pack_forget()
	else:
		TruthTableLbl.pack(anchor = "w", padx = 20, pady = 20)
	

def ShowVeitchDiagram(expr, frame):
	return

def MaximizeWindow(window):
	width = window.winfo_screenwidth()
	height = window.winfo_screenheight()
	window.geometry(str(width) + "x" + str(height))


def ShowEntryVar():
	global entryCnt
	entryCnt = (entryCnt + 1) % 2
	if entryCnt == 1:
		ShowEntryFuncBtn.config(anchor = "center", state = "normal", padx = 20, pady = 20)
	return


def ShowEntryFunc():
	return


def InputMethod(c, window, frame):
	if c == 1:
		OpenFile(window, frame)
	else:
		ManualInput(window, frame)

def ManualInput(window, frame):
	Clear(frame)

	CalcFrame = tk.Frame(window, bd = 1, relief = "sunken")
	CalcFrame.pack(side = "left", fill = "both", expand = True)


	FunctionLbl = tk.Label(CalcFrame, text = "Booleova funkcija u fileu je\nf( ) = ")
	MinimizedLbl = tk.Label(CalcFrame, text = "Minimizirana funkcija: ")

	MinimizeBtn = tk.Button(frame, text = "Minimizirana funkcija")
	ShowTruthBtn = tk.Button(frame, text = "Tablica istine")
	ShowVeitchBtn = tk.Button(frame, text = "Veitchev diagram")
	ClearBtn = tk.Button(frame, text = "Brisanje", command = lambda: Clear(CalcFrame, remain = [FunctionLbl]))
	BackBtn = tk.Button(frame, text = "Natrag", command = lambda: BackToBeginning(window, frame, CalcFrame))

	MinimizeBtn.pack(anchor = "w", padx = 20, pady = 20)
	ShowTruthBtn.pack(anchor = "w", padx = 20, pady = 20)
	ShowVeitchBtn.pack(anchor = "w", padx = 20, pady = 20)
	ClearBtn.pack(anchor = "w", padx = 20, pady = 20)
	FunctionLbl.pack(anchor = "center", padx = 20, pady = 20)
	BackBtn.pack(anchor = "w", padx = 20, pady = 20)


def OpenFile(window, frame):
	#fale komande za Minimizirana funkcija, Tablica istine i Veitchev diagram dovrsit

	#DELETE TOOLBAR WIDGETS
	Clear(frame)

	#SELECTION OF A FILE
	name = filedialog.askopenfilename(title = "Odaberite tekstualnu datoteku", filetypes = [("text files", "*.txt")])
	#size = len(name) - 4
	# cleanName = ""
	# for i in range(size):
	# 	if(name[size - i - 1] == '/'):
	# 		break
	# 	cleanName += name[size - 1 - i]
	# cleanName = cleanName[::-1]

	#INTERPRET FROM FILE
	with open(name, "r") as file:
		variables = file.readline()
		function = file.readline()


	expr = Formula(function, variables[:-1])

	CalcFrame = tk.Frame(window, bd = 1, relief = "sunken")
	CalcFrame.pack(side = "left", fill = "both", expand = True)


	FunctionLbl = tk.Label(CalcFrame, text = "Booleova funkcija u fileu je\nf(" + expr.variables + ") = " + expr.sentence)
	MinimizedLbl = tk.Label(CalcFrame, text = "Minimizirana funkcija: " + expr.sentence)

	MinimizeBtn = tk.Button(frame, text = "Minimizirana funkcija", command = lambda: ShowMinimized(CalcFrame, expr, MinimizedLbl))
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


def SaveFile():
	return

def SaveFileAs():
	return


def Help():
	messagebox.showinfo("Help", "Stisci botune pas vidit")

def About():
	messagebox.showinfo("About", "Seminarski rad iz kolegija OOP\nnapravio Vatroslav Bočkaj Bundara\nversion 1.0.0")

def ShowMinimized(frame, expr, lbl):
	global cnt
	cnt = (cnt + 1) % 2
	if cnt == 0:
		lbl.pack_forget()
	else:	
		lbl.pack(anchor = "w", padx = 20, pady = 20)


def CreateMenuBar(window, file = False, exit = False, win = False, info = False):
	NewMenuBar = tk.Menu(window)
	window.config(menu = NewMenuBar)

	#MENU BAR FILE
	if file == True:
		FileMenu = tk.Menu(NewMenuBar, tearoff = 0)
		FileMenu.add_command(label = "Save", command = lambda: SaveFile())
		FileMenu.add_command(label = "Save as", command = lambda: SaveFileAs())
		NewMenuBar.add_cascade(label = "File", menu = FileMenu)

	#MENU BAR EXIT
	if exit == True:
		ExitMenu = tk.Menu(NewMenuBar, tearoff = 0)
		ExitMenu.add_command(label = "Exit", command = window.destroy)
		NewMenuBar.add_cascade(label = "Exit", menu = ExitMenu)

	#MENU BAR INFO
	if info == True:
		InfoMenu = tk.Menu(NewMenuBar, tearoff = 0)
		InfoMenu.add_command(label = "Help", command = Help)
		InfoMenu.add_command(label = "About", command = About)
		NewMenuBar.add_cascade(label = "Info", menu = InfoMenu)

	#MENU BAR WINDOW
	if win == True:
		WindowMenu = tk.Menu(NewMenuBar, tearoff = 0)
		WindowMenu.add_command(label = "Minimize", command = lambda: window.geometry("300x300"))
		WindowMenu.add_command(label = "Maximize", command = lambda: MaximizeWindow(window))
		NewMenuBar.add_cascade(label = "Window", menu = WindowMenu)

























