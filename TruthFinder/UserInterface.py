from MenuLogic import *
from tkinter import ttk


MainWindow = tk.Tk()
MainWindow.title("TruthFinder")
MainWindow.geometry("300x200")
MainWindow.iconbitmap("logo.ico")

MenuBar = tk.Menu(MainWindow)
MainWindow.config(menu = MenuBar)


#MENU BAR FILE
FileMenu = tk.Menu(MenuBar, tearoff = 0)
FileMenu.add_command(label = "Open", command = lambda: OpenFile(MainWindow))
FileMenu.add_command(label = "Save", command = lambda: SaveFile())
FileMenu.add_command(label = "Save as", command = lambda: SaveFileAs())
FileMenu.add_command(label = "New", command = lambda: NewFile())
MenuBar.add_cascade(label = "File", menu = FileMenu)

#MENU BAR EXIT
ExitMenu = tk.Menu(MenuBar, tearoff = 0)
ExitMenu.add_command(label = "Exit", command = MainWindow.quit)
MenuBar.add_cascade(label = "Exit", menu = ExitMenu)

#MENU BAR INFO
InfoMenu = tk.Menu(MenuBar, tearoff = 0)
InfoMenu.add_command(label = "Help", command = Help)
InfoMenu.add_command(label = "About", command = About)
MenuBar.add_cascade(label = "Info", menu = InfoMenu)


MainWindow.mainloop()

