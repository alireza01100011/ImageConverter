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
        
        FreameButtomFormatOutPut = Frame(self.root , width=400 , height=200 , bg='#48E6E1')
        FreameButtomFormatOutPut.pack(side=TOP)

        FreameINPandOUT = Frame(self.root , width=400 , height=150 , bg='#48E6E1')
        FreameINPandOUT.pack(side=TOP)

        FreameSTART = Frame(self.root , width=400 , height=150  , bg='#48E6E1')
        FreameSTART.pack(side=TOP)

        self.root.mainloop()
    

test = GUI()
test.LoadRootWindows()