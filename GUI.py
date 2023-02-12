from tkinter import * 
import tkinter.font as font
from tkinter import ttk
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
        self.FreameButtomFormatOutPut = Frame(self.root , width=400 , height=200 , bg='#48E6E1')
        self.FreameButtomFormatOutPut.pack(side=TOP)

        self.FreameINPandOUT = Frame(self.root , width=400 , height=150 , bg='#48E6E1')
        self.FreameINPandOUT.pack(side=TOP)

        self.FreameSTART = Frame(self.root , width=400 , height=150  , bg='#48E6E1')
        self.FreameSTART.pack(side=TOP)

        FontButton = font.Font(family='Comic Sans MS', size=20, weight='bold')

        # ### === >  Buttons < ==== ### #
        # JPG
        self.Button_JPG = Button(self.FreameButtomFormatOutPut , text='JPG' , bg='#66FFFF'  , width=4 , height=1 , font=FontButton)
        self.Button_JPG.place(x=30 , y=80)
        # PNG
        self.Button_PNG = Button(self.FreameButtomFormatOutPut , text='PNG' , bg='#33FFFF'  , width=4 , height=1 , font=FontButton)
        self.Button_PNG.place(x=170 , y=80)
        # WEBP
        self.Button_WEBP = Button(self.FreameButtomFormatOutPut , text='WEBP' , bg='#00FFFF'  , width=4 , height=1 , font=FontButton)
        self.Button_WEBP.place(x=300 , y=80)
        # Select Images
        FontButtonINPandOUT = font.Font(family='Comic Sans MS', size=10)
        self.Button_SelectImages = Button(self.FreameINPandOUT , text='Selection' , bg='#27E48C'  , width=8 , height=1 , font=FontButtonINPandOUT)
        self.Button_SelectImages.place(x=305 , y=20)
        # Seve Path
        self.Button_Seve = Button(self.FreameINPandOUT , text='Seve' , bg='#27E48C'  , width=8 , height=1 , font=FontButtonINPandOUT)
        self.Button_Seve.place(x=305 , y=100)
        # Start Button
        self.Button_Seve = Button(self.FreameSTART , text='Start' , bg='#FFFFFF'  , width=6 , height=2 , font=font.Font(family='Comic Sans MS', size=12, weight='bold'))
        self.Button_Seve.place(x=310 , y=50)

        # ### === >  Labels (Text) < ==== ### #
        Label(self.FreameButtomFormatOutPut , text='Which Format Should Your Images Be Converted To ? ' , bg='#48E6E1' , font=font.Font(family='Comic Sans MS', size=10 , weight='bold')).place(x=30 , y=20)
        
        self.Label_SelectImage = Label(self.FreameINPandOUT , text='Choose The Images You Want >> ' , bg='#48E6E1' , font=font.Font(family='Comic Sans MS', size=10 , weight='bold'))
        self.Label_SelectImage.place(x=30 , y=20)
        
        self.Label_PathSeve = Label(self.FreameINPandOUT , text='Where To Save The Results ?  >> ' , bg='#48E6E1' , font=font.Font(family='Comic Sans MS', size=10 , weight='bold'))
        self.Label_PathSeve.place(x=30 , y=100)
        
        self.Label_ShowLog = Label(self.FreameSTART , text='Log ....................................' , bg='#48E6E1' , font=font.Font(family='Comic Sans MS', size=10 , weight='bold'))
        self.Label_ShowLog.place(x=30 , y=110)
        
        # ### === >  Progressbar < ==== ### #
        self.Proses = ttk.Progressbar(self.FreameSTART , orient=HORIZONTAL , length=250  , mode='determinate')
        self.Proses.place(x=30,y=60 , height=40)

        
        self.root.mainloop()
    
        
test = GUI()
Thread(target=test.LoadRootWindows).start()
