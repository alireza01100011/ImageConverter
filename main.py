from PIL import Image
from tkinter import filedialog
import PIL
import os
import glob
import time
import concurrent.futures


class ConvertImage():
    def __init__(self , PathInputFolder , PathOutputFolder , ForamtOutput , FAST=True) -> None:
        self.FAST = FAST
        self.PathInput = PathInputFolder
        self.PathOutput = PathOutputFolder
        self.FormatsInput  = ('jpg' , 'png' , 'webp')
        self.FormatsOutput = ('jpg' , 'png' , 'webp')
        self.FormatOutout = ForamtOutput
    
    def FindImages(self):
        # Get the files and folders in the input folder
        ListDir = os.listdir(self.PathInput)
        
        Images = list()
        # Filter photos
        for item in ListDir :
            item = item.split('.')
            if item[-1] in self.FormatsInput:
                name = ''
                for l in item[:-1]: name += '.' + l
                name = name[1:]
                Images.append((name,item[-1]))
        
        self.Images = Images
    def ConvertImage(self , Photo):
        try :
            # Open The Image
            Img = Image.open(f'{self.PathInput}/{Photo[0]}.{Photo[1]}')
            # Convert the image to RGB Colour
            Img = Img.convert('RGB')
            # Save The Image
            Img.save(f'{self.PathOutput}/{Photo[0]}.{self.FormatOutout}' , self.FormatOutout)
        except OSError : return False
    
    def Run(self):
        if self.FAST == True:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                Tasks = [executor.submit(self.ConvertImage , img) for img in self.Images]

                for task in Tasks:
                    task.result()
        elif self.FAST == False :
            for img in self.Images:
                self.ConvertImage(img)
        
        else :
            return


PathInput = filedialog.askdirectory(title="Select Drictory For Save")
PathOutput = filedialog.askdirectory(title="Select Drictory For Save")
test = ConvertImage(PathInput , PathOutput , 'webp')
Start = time.time()
test.FindImages()
print(test.Images[1])
test.Run()
print(time.time() - Start)