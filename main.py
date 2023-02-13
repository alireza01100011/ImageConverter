# https://github.com/alireza536
# Python 3.10.5 64bit

from PIL import Image
from tkinter import filedialog
import tkinter.filedialog as fd
import concurrent.futures


class ConvertImage():
    def __init__(self , ImagesPath, PathOutputFolder , ForamtOutput , FAST=True , Images=dict()) -> None:
        self.FAST = FAST
        # self.PathInput = PathInputFolder # (This feature will be added in future updates)
        self.PathOutput = PathOutputFolder
        self.FormatsInput  = ('jpg' , 'png' , 'webp')
        self.FormatsOutput = ('jpg' , 'png' , 'webp')
        self.FormatOutout = ForamtOutput
        self.Images = Images
        self.ImagesPath = ImagesPath
        self.Log = ''
        self.Progress = 0

    # Extract images from the folder (This feature will be added in future updates)
    # def FindImages(self):
    #     # Get the files and folders in the input folder
    #     ListDir = os.listdir(self.PathInput)
        
    #     # Filter photos
    #     for item in ListDir :
    #         item = item.split('.')
    #         if item[-1] in self.FormatsInput:
    #             name = ''
    #             for l in item[:-1]: name += '.' + l
    #             name = name[1:]
                
    #             self.Images[str(name)] = {
    #                 'name' : name ,
    #                 'path' : f'{self.PathInput}/{name}.{item[-1]}',
    #                 'format' : item[-1]
    #                 }

    def OrganizeImagesAddress(self):
        for item in self.ImagesPath :
            
            item = item.split('.')
            if item[-1] in self.FormatsInput:
                name = ''
                for l in item[:-1]: name += '.' + l
                name = name[1:]
                
                self.Images[str(name)] = {
                    'name' : name.split('/')[-1] ,
                    'path' : f'{name}.{item[-1]}',
                    'format' : item[-1]
                    }

    def ConvertImage(self , Photo):
        try :
            self.Progress += 100 / len(self.Images)
            self.Log = (f'Start {Photo["name"]} Photo Processing ')
            # Open The Image
            Img = Image.open(Photo['path'])
            # Convert the image to RGB Colour
            Img = Img.convert('RGB')
            # Save The Image
            Img.save(f'{self.PathOutput}/{Photo["name"]}.{self.FormatOutout}' , self.FormatOutout)
            self.Log = f'Image Of {Photo["name"]} Was Processed Successfully '
        except OSError : self.Log = f'A Problem Occurred While Processing The Image Of {Photo["name"]} !' ; return False
    
    def Run(self):
        if self.FAST == True:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                Tasks = [executor.submit(self.ConvertImage , img) for img in self.Images.values()]

                for task in Tasks:
                    task.result()
        elif self.FAST == False :
            for img in self.Images:
                self.ConvertImage(img)
        
        else :
            return

if __name__ == '__main__':

    InPath = fd.askopenfilenames(title='Choose a file' ,  filetypes=[
                        ("All Images", ".jpg"),("All Images", ".png"),("All Images", ".webp"),
                        ("JPG", ".jpg"),("PNG", ".png"),("WEBP", ".webp"),])

    print(InPath)
    OutPath = filedialog.askdirectory(title="Select Drictory For Save")
    test = ConvertImage(ImagesPath=InPath , PathOutputFolder=OutPath , ForamtOutput='webp')
    test.OrganizeImagesAddress()
    print(test.Images)
    print(OutPath)
    test.Run()