
from MenuLogic import *
import os

MainWindow = tk.Tk()
MainWindow.title("TruthFinder")
MainWindow.geometry("800x400")
#MainWindow.iconbitmap("logo.ico")

ToolBar = tk.Frame(MainWindow, bd = 1, relief = "sunken")
choice = tk.IntVar(value = -1)

logo = tk.PhotoImage(file = os.path.join("/", "Users", "quomod0", "Desktop", "OOP_seminarski", "grafika", "TTLogo.png"))
logoLbl = tk.Label(ToolBar, image = logo)
logoLbl.pack(anchor = "nw", padx = 20)

ManualBtn = tk.Radiobutton(ToolBar, text = "Manualan unos", value = -1, variable = choice)
FromFileBtn = tk.Radiobutton(ToolBar, text = "Unos iz datoteke", value = 1, variable = choice)
#FromTruthTableBtn = tk.Radiobutton(ToolBar, text = "Unos iz tablice istine", value = 2, variable = choice)
EnterBtn = tk.Button(ToolBar, text = "Zaključaj odabir", command = lambda: InputMethod(choice.get(), MainWindow, ToolBar, logo))

ManualBtn.pack(anchor = "center", padx = 20)
FromFileBtn.pack(anchor = "center", padx = 20)
#FromTruthTableBtn.pack(anchor = "center", padx = 20)
EnterBtn.pack(anchor = "center", padx = 20, pady = 20)
ToolBar.pack(side = "left", fill = "y")


CreateMenuBar(MainWindow, exit = True, win = True, info = True)

MainWindow.mainloop()






