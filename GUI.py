from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from threading import Thread

import tkinter.font as font
import tkinter.filedialog as fd
import webbrowser
import main
import os
import time

class GUI():
    def __init__(self) -> None:
        self.ForamtOutput = None
        self.PathOutputFolder = None
        self.Images = None
    
    def callback(self , url): webbrowser.open_new(url)

    def _FillingAnimation(self):  
        for s in range(100) : self.Proses['value'] = s ; time.sleep(0.008)

    def SetForamtOutput(self , Extension , Button):
        # Buttons With Color Code
        ButtonsFormat = ((self.Button_JPG , '#66FFFF') , (self.Button_PNG  , '#33FFFF'), (self.Button_WEBP , '#00FFFF' ))
        
        # Set The Output Extension 
        self.ForamtOutput = Extension
        
        # Change The Color Of The Buttons 
        for button in ButtonsFormat:
            if button[0] == Button : Button['bg'] = '#FFFF00'
            else : button[0]['bg'] = button[1]
                
    def SelectImages(self):
        images = fd.askopenfilenames(title='Choose a file' ,  filetypes=[
                        ("All Images", ".jpg"),("All Images", ".png"),("All Images", ".webp"),
                        ("JPG", ".jpg"),("PNG", ".png"),("WEBP", ".webp"),])
        if len(images) == 0 : return
        self.Images = images
        # Size Calculation
        Total , Size = 0 , 0
        for img in images : Total , Size = Total + 1 , Size + os.path.getsize(img)
        Size = (Size / 1024) / 1024
        self.Label_TotalImagesAndSize = Label(self.FreameINPandOUT , text=f'Total : {Total} {" "* ( 10 - len(str(Total)))} Size : {round(Size , 2)} MB' , bg='#48E6E1' , font=font.Font(family='Comic Sans MS', size=10 , weight='bold'))
        self.Label_TotalImagesAndSize.place(x=30 , y=50)
    
    def ChooseDirectorySave(self):
        path = filedialog.askdirectory(title="Select Drictory For Save")
        if len(path) == 0: print('None') ; return
        self.PathOutputFolder = path
        self.Label_ShowPathOutputFolder = Label(self.FreameINPandOUT , text=self.PathOutputFolder , bg='#48E6E1' , font=font.Font(family='Comic Sans MS', size=10 , weight='bold'))
        self.Label_ShowPathOutputFolder.place(x=30 , y=130)
    
    def UpdateGUI(self):
        while self._RunUpdate:
            self.Proses['value'] = self.Convert.Progress
            self.Label_ShowLog['text'] = self.Convert.Log

    def Start(self):
        if self.ForamtOutput == None: self.Label_ShowLog['text'] = 'Please Specify The Output Format (JPG , PNG , WEBP)' ; self.Label_ShowLog['fg'] = 'red' ; return False
        elif self.PathOutputFolder == None : self.Label_ShowLog['text'] = 'Please Specify The Storage Location (Seve)' ; self.Label_ShowLog['fg'] = 'red' ; return False
        elif self.Images == None : self.Label_ShowLog['text'] = 'Please Select Images (Selection)' ; self.Label_ShowLog['fg'] = 'red' ; return False
        else :  self.Label_ShowLog['text'] = 'Starting Conversion ...' ; self.Label_ShowLog['fg'] = '#000000'
        
        Thread(target= self._FillingAnimation).start()
        
        self.Convert = main.ConvertImage(ImagesPath=self.Images , PathOutputFolder=self.PathOutputFolder , ForamtOutput=self.ForamtOutput)
        self.Convert.OrganizeImagesAddress()
        
        Run = Thread(target= self.Convert.Run)
        Run.start()
        print('Start')
        self._RunUpdate = True
        Thread(target= self._FillingAnimation).start()
        Thread(target= self.UpdateGUI).start()
        Run.join()
        self._RunUpdate = False
        Thread(target= self._FillingAnimation).start()
        self.Proses['value'] = 100
        self.Label_ShowLog['text'] = 'Done ! '
            
    def LoadRootWindows(self):
        self.root = Tk()
        self.root.geometry('400x550')
        self.root.title('Image Converter')
        self.root.config(bg='#48E6E1')
        self.root.resizable(False , False)
        
        # ### === >  Freames < ==== ### #
        self.FreameButtomFormatOutPut = Frame(self.root , width=400 , height=200 , bg='#48E6E1')
        self.FreameButtomFormatOutPut.pack(side=TOP)

        self.FreameINPandOUT = Frame(self.root , width=400 , height=150 , bg='#48E6E1')
        self.FreameINPandOUT.pack(side=TOP)

        self.FreameSTART = Frame(self.root , width=400 , height=200  , bg='#48E6E1')
        self.FreameSTART.pack(side=TOP)

        FontButton = font.Font(family='Comic Sans MS', size=20, weight='bold')

        # ### === >  Buttons < ==== ### #
        # JPG
        self.Button_JPG = Button(self.FreameButtomFormatOutPut , text='JPG' , bg='#66FFFF'  , width=4 , height=1 , font=FontButton , command=lambda : self.SetForamtOutput('jpg' , self.Button_JPG))
        self.Button_JPG.place(x=30 , y=80)
        # PNG
        self.Button_PNG = Button(self.FreameButtomFormatOutPut , text='PNG' , bg='#33FFFF'  , width=4 , height=1 , font=FontButton , command=lambda : self.SetForamtOutput('png' , self.Button_PNG))
        self.Button_PNG.place(x=170 , y=80)
        # WEBP
        self.Button_WEBP = Button(self.FreameButtomFormatOutPut , text='WEBP' , bg='#00FFFF'  , width=4 , height=1 , font=FontButton , command=lambda : self.SetForamtOutput('webp' , self.Button_WEBP))
        self.Button_WEBP.place(x=300 , y=80)
        # Select Images
        FontButtonINPandOUT = font.Font(family='Comic Sans MS', size=10)
        self.Button_SelectImages = Button(self.FreameINPandOUT , text='Selection' , bg='#27E48C'  , width=8 , height=1 , font=FontButtonINPandOUT , command=lambda : Thread(target=self.SelectImages).start())
        self.Button_SelectImages.place(x=305 , y=20)
        # Seve Path
        self.Button_Seve = Button(self.FreameINPandOUT , text='Seve' , bg='#27E48C'  , width=8 , height=1 , font=FontButtonINPandOUT , command=lambda : Thread(target=self.ChooseDirectorySave).start() )
        self.Button_Seve.place(x=305 , y=100)
        # Start Button
        self.Button_Start = Button(self.FreameSTART , text='Start' , bg='#FFFFFF'  , width=6 , height=2 , font=font.Font(family='Comic Sans MS', size=12, weight='bold') , command=lambda : Thread(target=self.Start).start())
        self.Button_Start.place(x=310 , y=50)

        # ### === >  Labels (Text) < ==== ### #
        Label(self.FreameButtomFormatOutPut , text='Which Format Should Your Images Be Converted To ? ' , bg='#48E6E1' , font=font.Font(family='Comic Sans MS', size=10 , weight='bold')).place(x=30 , y=20)
        
        self.Label_SelectImage = Label(self.FreameINPandOUT , text='Choose The Images You Want >> ' , bg='#48E6E1' , font=font.Font(family='Comic Sans MS', size=10 , weight='bold'))
        self.Label_SelectImage.place(x=30 , y=20)

        self.Label_PathSeve = Label(self.FreameINPandOUT , text='Where To Save The Results ?  >> ' , bg='#48E6E1' , font=font.Font(family='Comic Sans MS', size=10 , weight='bold'))
        self.Label_PathSeve.place(x=30 , y=100)
        
        self.Label_CPU = Label(self.FreameSTART , text='This Program Uses All The Power Of Your CPU For Higher Speed ' , bg='#48E6E1' , fg='red' , font=font.Font(family='Comic Sans MS', size=8 , weight='bold'))
        self.Label_CPU.place(x=20 , y=10)
        
        self.Label_ShowLog = Label(self.FreameSTART , text='' , bg='#48E6E1' , font=font.Font(family='Comic Sans MS', size=10 , weight='bold'))
        self.Label_ShowLog.place(x=30 , y=120)
        
        # ### === >  Progressbar < ==== ### #
        self.Proses = ttk.Progressbar(self.FreameSTART , orient=HORIZONTAL , length=250  , mode='determinate')
        self.Proses.place(x=30,y=60 , height=40)

        # ### === >  Links < ==== ### #
        DeveloperPage = Label(self.FreameSTART, text="Developer", bg='#48E6E1', fg="#000000", cursor="hand2" , font=font.Font(family='Comic Sans MS', size=10 , weight='bold'))
        DeveloperPage.place(x=310 , y=160)
        DeveloperPage.bind("<Button-1>", lambda e: self.callback("https://github.com/alireza536"))

        SourceCode = Label(self.FreameSTART, text="Source Code", bg='#48E6E1', fg="#000000", cursor="hand2" , font=font.Font(family='Comic Sans MS', size=10 , weight='bold'))
        SourceCode.place(x=155 , y=160)
        SourceCode.bind("<Button-1>", lambda e: self.callback("https://github.com/alireza536/ImageConverter"))

        Update = Label(self.FreameSTART, text="Update", bg='#48E6E1', fg="#000000", cursor="hand2" , font=font.Font(family='Comic Sans MS', size=10 , weight='bold'))
        Update.place(x=30 , y=160)
        Update.bind("<Button-1>", lambda e: self.callback("https://github.com/alireza536/ImageConverter"))
        
        self.root.mainloop()
    
        
test = GUI()
test.LoadRootWindows()
