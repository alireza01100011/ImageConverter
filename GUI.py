from tkinter import *
import tkinter.font as font

from threading import Thread

class GUI():
    def __init__(self) -> None:
        pass

    def LoadRootWindows(self):
        self.root = Tk()
        self.root.geometry('400x500')
        self.root.title('Image Converter')
        self.root.config(bg='#48E6E1')
        self.root.resizable(False , False)
        
        self.root.mainloop()
    

test = GUI()
test.LoadRootWindows()