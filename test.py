import defines, PIL
from tkinter import filedialog
from tkinter import *

start = Tk()
start.withdraw()
defines.loadImg()
loadGui = filedialog.askopenfilename(initialdir = "/home",title = "IMAGE SELECTION",filetypes = (("JPEG files","*.jpg"),("PNG files","*.png"))) # set up the gui
useImg = PIL.Image.open(loadGui)

modDiag = input('Do you want to modify the image?\nY | N\n')
if modDiag == 'Y' or modDiag == 'y':
	saveGui = filedialog.asksaveasfilename(initialdir = "/home",title = "IMAGE SELECTION",filetypes = (("JPEG files","*.jpg"),("PNG files","*.png")))
	img.PIL.save(saveGui)
