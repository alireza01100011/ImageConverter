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
        pass
    def ConvertImage(self , Photo):
        pass
    
    def Run(self):
        pass


