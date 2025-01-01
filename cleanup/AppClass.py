
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from BooleanFunctionClass import*


def Help():
	messagebox.showinfo("Pomoć", "Pritiskom na opciju manualnog unosa mozete manualno unijeti booleovu funkciju, a opcijom čitanja iz datoteke booleova funkcija se pročita iz odabrane datoteke")

def About():
	messagebox.showinfo("Više o", "Seminarski rad iz kolegija OOP\nnapravio Vatroslav Bočkaj Bundara\nversion 1.1")

def MaximizeWindow(window):
	window.attributes("-fullscreen", True)

def MinimizeWindow(window):
	window.attributes("-fullscreen", False)
	window.geometry("300x400")




class App:

	def __init__(self, window):
		#prozor
		self.window = window
		self.window.geometry("400x600")
		self.window.title("Seminarski OOP")

		#menubar
		self.menubar = tk.Menu(self.window)
		self.window.config(menu = self.menubar)
		self.infomenu = tk.Menu(self.menubar, tearoff = 0)
		self.exitmenu = tk.Menu(self.menubar, tearoff = 0)
		self.windowmenu = tk.Menu(self.menubar, tearoff = 0)
		self.infomenu.add_command(label = "Pomoć", command = Help)
		self.infomenu.add_command(label = "O aplikaciji", command = About)
		self.exitmenu.add_command(label = "Izlaz", command = self.window.destroy)
		self.windowmenu.add_command(label = "Minimiziraj", command = lambda: MinimizeWindow(self.window))
		self.windowmenu.add_command(label = "Maksimiziraj", command = lambda: MaximizeWindow(self.window))
		self.menubar.add_cascade(label = "Izlaz", menu = self.exitmenu)
		self.menubar.add_cascade(label = "Info", menu = self.infomenu)
		self.menubar.add_cascade(label = "Prozor", menu = self.windowmenu)


		self.toolbar = tk.Frame(window, bd = 1, relief = "sunken")
		self.calcScreen = tk.Frame(window, bd = 1, relief = "sunken")

		self.inputChoice = tk.IntVar(value = -1)

		#funkcija u apk
		self.function = Formula("!x", "x")

		#stanja
		self.truthTableUsed = False
		self.minimizeUsed = False

		#file
		self.newFile = ""

		#prikaz teksta
		self.varsLbl = tk.Label(self.calcScreen, text = "Ovdje unesite varijable (min. 1, max. 5), dopustena su samo velika i mala slova")
		self.funcLbl = tk.Label(self.calcScreen, text = "Ovdje unesite booleovu funkciju\n - negacija '!'\n - konjunkcija '&'\n - disjunkcija '|'\n - pisite sve skupa")
		self.minimizeLbl = tk.Label(self.calcScreen, text = "Minimizirana funkcija: " + self.function.CalcMinimal())
		self.displayFuncLbl = tk.Label(self.calcScreen, text = "Trenutna funkcija je: f(" + self.function.variables + ") = " + self.function.sentence)

		#tekstualni unos
		self.varsEntry = tk.Entry(self.calcScreen, width = 15, relief = "sunken")
		self.funcEntry = tk.Entry(self.calcScreen, width = 40, relief = "sunken")

		#botuni
		self.manualBtn = tk.Radiobutton(self.toolbar, text = "Manualan unos", value = 0, variable = self.inputChoice)
		self.fileBtn = tk.Radiobutton(self.toolbar, text = "Unos iz datoteke", value = 1, variable = self.inputChoice)
		self.enterBtn = tk.Button(self.toolbar, text = "Zaključaj odabir", command = lambda: self.InputMethod())
		self.enterFuncBtn = tk.Button(self.toolbar, text = "Unesi funkciju", command = lambda: self.EnterFunc())
		self.minimizeBtn = tk.Button(self.toolbar, text = "Minimiziraj", command = lambda: self.MinimizeFunc())
		self.truthTableBtn = tk.Button(self.toolbar, text = "Tablica istine", command = lambda: self.TruthTableFunc())
		self.clearBtn = tk.Button(self.toolbar, text = "Briši", command = lambda: self.Hide(self.calcScreen, show = [self.funcEntry, self.varsEntry, self.funcLbl, self.varsLbl]))
		self.saveBtn = tk.Button(self.toolbar, text = "Spremi", command = lambda: self.Save())
		self.saveAsBtn = tk.Button(self.toolbar, text = "Spremi kao", command = lambda: self.SaveAs())
		self.backBtn = tk.Button(self.toolbar, text = "Natrag", command = lambda: self.Back())

		#tablice
		self.truthTable = ttk.Treeview(self.calcScreen, columns = self.function.TT[0], show = "headings", height = len(self.function.TT))


	def Reset(self):
		self.truthTableUsed = False
		self.minimizeUsed = False


	# def Clear(self, frame, remain = []):
	# 	self.Reset()

	# 	for widget in frame.winfo_children():
	# 		inside = widget in remain
	# 		if inside == False:
	# 			widget.destroy()


	def Hide(self, frame, show = []):
		self.Reset()

		for widget in frame.winfo_children():
			if not widget in show:
				widget.pack_forget()


	def Back(self):
		self.Hide(self.toolbar)
		self.Hide(self.calcScreen)
		self.startOption()


	def EnterFunc(self):
		self.function = Formula(self.funcEntry.get(), self.varsEntry.get())

		if self.function.CheckVars() == False:
			messagebox.showerror("Greška", "Varijable krivo upisane")
		elif self.function.valid == False:
			messagebox.showerror("Greška", "Neispravna sintaksa funkcije")


	def MinimizeFunc(self):
		if self.minimizeUsed == False:

			self.minimizeUsed = True

			self.minimizeLbl.config(text = "Minimizirana funkcija: " + self.function.CalcMinimal())
			self.minimizeLbl.pack(anchor = "w", padx = 20, pady = 20)


	def TruthTableFunc(self):
		# for row in self.function.TT:
		# 	print(*row)

		if self.truthTableUsed == False:

			self.truthTableUsed = True

			self.truthTable.config(columns = self.function.TT[0], show = "headings", height = len(self.function.TT))

			for H in self.function.TT[0]:
				self.truthTable.heading(H, text = H)
				self.truthTable.column(H, width = 10, anchor = "center")

			for row in self.function.TT[1:]:
				self.truthTable.insert("", "end", values = row)

			self.truthTable.pack(fill = "both")


	def Save(self):
		return


	def SaveAs(self):
		return


	def ManualInput(self):
		self.Hide(self.toolbar)

		self.varsLbl.pack(anchor = "center", padx = 20, pady = 5)
		self.varsEntry.pack(anchor = "center", padx = 20, pady = 5)
		self.funcLbl.pack(anchor = "center", padx = 20, pady = 5)
		self.funcEntry.pack(anchor = "center", padx = 20, pady = 5)
		self.calcScreen.pack(side = "left", fill = "both", expand = True)

		self.enterFuncBtn.pack(anchor = "w", padx = 20, pady = 20)
		self.minimizeBtn.pack(anchor = "w", padx = 20, pady = 20)
		self.truthTableBtn.pack(anchor = "w", padx = 20, pady = 20)
		self.clearBtn.pack(anchor = "w", padx = 20, pady = 20)
		self.saveBtn .pack(anchor = "w", padx = 20, pady = 20)
		self.saveAsBtn.pack(anchor = "w", padx = 20, pady = 20)
		self.backBtn.pack(anchor = "w", padx = 20, pady = 20)


	def FileInput(self):
		self.Hide(self.toolbar)

		self.newFile = filedialog.askopenfilename(title = "Odaberite tekstualnu datoteku", filetypes = [("tekstualne datoteke", "*.txt")])

		if self.newFile == "":
			return self.startOption()

		with open(self.newFile, "r") as file:
			varz = file.readline()
			func = file.readline()

		self.function = Formula(func, varz[:-1])

		self.displayFuncLbl.config(text = "Trenutna funkcija je: f(" + self.function.variables + ") = " + self.function.sentence)

		self.calcScreen.pack(side = "left", fill = "both", expand = True)
		self.minimizeBtn.pack(anchor = "w", padx = 20, pady = 20)
		self.truthTableBtn.pack(anchor = "w", padx = 20, pady = 20)
		self.clearBtn.pack(anchor = "w", padx = 20, pady = 20)
		self.backBtn.pack(anchor = "w", padx = 20, pady = 20)

		self.displayFuncLbl.pack(anchor = "center", padx = 20, pady = 20)


	def InputMethod(self):
		if self.inputChoice.get() == 0:
			self.ManualInput()
		elif self.inputChoice.get() == 1:
			self.FileInput()
		return


	def startOption(self):
		self.Hide(self.toolbar)
		self.Hide(self.calcScreen)


		self.manualBtn = tk.Radiobutton(self.toolbar, text = "Manualan unos", value = 0, variable = self.inputChoice)
		self.fileBtn = tk.Radiobutton(self.toolbar, text = "Unos iz datoteke", value = 1, variable = self.inputChoice)
		self.enterBtn = tk.Button(self.toolbar, text = "Zaključaj odabir", command = lambda: self.InputMethod())

		self.manualBtn.pack(anchor = "center", padx = 20)
		self.fileBtn.pack(anchor = "center", padx = 20)
		self.enterBtn.pack(anchor = "center", padx = 20, pady = 20)
		self.toolbar.pack(side = "left", fill = "y")





window = tk.Tk()

apk = App(window)

apk.startOption()

window.mainloop()





