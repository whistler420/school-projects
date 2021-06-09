import PIL.Image
from tkinter import filedialog as File #shamelessly stolen from test.py
from tkinter import *
startTk = Tk()
startTk.withdraw()
error = True
while error == True:
	usrIn = print('Please select an image file.')
	loadGui = filedialog.askopenfilename(initialdir = "/home/whistler/import",title = "IMAGE SELECTION",filetypes = (("All files","*.*"),("JPEG files","*.jpg *.JPEG"),("PNG files","*.png *.PNG"),("BMP files","*.bmp *.BMP")))
	error = False
	try:
		img = PIL.Image.open(loadGui)
	except AttributeError:
		sys.exit()
	except:
		print('Please try again.')
		error = True
