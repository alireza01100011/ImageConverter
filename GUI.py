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
        
        # ### === >  Freames < ==== ### #
        FreameButtomFormatOutPut = Frame(self.root , width=400 , height=200 , bg='#48E6E1')
        FreameButtomFormatOutPut.pack(side=TOP)

        FreameINPandOUT = Frame(self.root , width=400 , height=150 , bg='#48E6E1')
        FreameINPandOUT.pack(side=TOP)

        FreameSTART = Frame(self.root , width=400 , height=150  , bg='#48E6E1')
        FreameSTART.pack(side=TOP)

        FontButton = font.Font(family='Comic Sans MS', size=20, weight='bold')

        # ### === >  Buttons < ==== ### #
        # JPG
        Button_JPG = Button(FreameButtomFormatOutPut , text='JPG' , bg='#A527E4'  , width=4 , height=1 , font=FontButton)
        Button_JPG.place(x=30 , y=80)
        # PNG
        Button_PNG = Button(FreameButtomFormatOutPut , text='PNG' , bg='#A527E4'  , width=4 , height=1 , font=FontButton)
        Button_PNG.place(x=170 , y=80)
        # WEBP
        Button_WEBP = Button(FreameButtomFormatOutPut , text='WEBP' , bg='#A527E4'  , width=4 , height=1 , font=FontButton)
        Button_WEBP.place(x=300 , y=80)
        # Select Images
        FontButtonINPandOUT = font.Font(family='Comic Sans MS', size=10)
        Button_SelectImages = Button(FreameINPandOUT , text='Selection' , bg='#27E48C'  , width=8 , height=1 , font=FontButtonINPandOUT)
        Button_SelectImages.place(x=305 , y=20)
        # Seve Path
        Button_Seve = Button(FreameINPandOUT , text='Seve' , bg='#27E48C'  , width=8 , height=1 , font=FontButtonINPandOUT)
        Button_Seve.place(x=305 , y=100)
        # Start Button
        Button_Seve = Button(FreameSTART , text='Start' , bg='#FFFFFF'  , width=6 , height=2 , font=font.Font(family='Comic Sans MS', size=12, weight='bold'))
        Button_Seve.place(x=310 , y=50)

    
        self.root.mainloop()
    

test = GUI()
test.LoadRootWindows()