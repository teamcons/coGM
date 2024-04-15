#!/usr/bin/env python3


import sys

from tkinter import *
from tkinter.ttk import *


# Same as Powershell
MainWindow = Tk()
MainWindow.title("Window With a Title Bar")
#MainWindow.iconbitmap('./assets/pythontutorial.ico')

MainWindow.geometry("600x400")


MainWindow.rowconfigure(0, minsize=50, weight=1)
MainWindow.columnconfigure([0, 1, 2], minsize=50, weight=1)



# Basically ShowDialog()
MainWindow.mainloop()