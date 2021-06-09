"""
VHS SCRIPT DEMO THINGY LOL
MADE USING XUBUNTU 19.04 OCT-2019
"""

import PIL.Image as PImage
import PIL.ImageCms as PImageCms
from tkinter import filedialog as File #shamelessly stolen from test.py BECAUSE IT JUST WORKS GOGAMMIT
from tkinter import *
startTk = Tk()
startTk.withdraw()
error = True
while error == True:
	usrIn = print('Please select an image file.')
	loadGui = filedialog.askopenfilename(initialdir = "/home/",title = "IMAGE SELECTION",filetypes = (("All files","*.*"),("JPEG files","*.jpg *.JPEG"),("PNG files","*.png *.PNG"),("BMP files","*.bmp *.BMP")))
	error = False
	try:
		img = PImage.open(loadGui)
		x = img.size[0]
		y = img.size[1]
	except AttributeError:
		sys.exit()
	except:
		print('Please try again.')
		error = True
	print("Now converting...") 
	srgbP = PImageCms.createProfile("sRGB")
	labP = PImageCms.createProfile("LAB")
	conver = PImageCms.buildTransformFromOpenProfiles(srgbP,labP,"RGB","LAB")
	VHS = PImageCms.applyTransform(img,conver) # convert to LAB color
	L,a,b = VHS.split()  # split L and AB into separate files
	vhsLP1 = L.resize([333,480],resample=PImage.LANCZOS).convert("RGBA") # resize L
	vhsAP1 = a.resize([40,480],resample=PImage.LANCZOS).convert("RGBA") 
	vhsBP1 = b.resize([40,480],resample=PImage.LANCZOS).convert("RGBA") # resize AB
	nLoad = PImage.open("/home/whistler/import/noise.png").convert("RGBA")
	nLoad2 = PImage.open("/home/whistler/import/noiseBig.png").convert("RGBA")
	vhsLTST = PImage.alpha_composite(vhsLP1,nLoad2)
	vhsAP2 = PImage.alpha_composite(vhsAP1,nLoad) # add noise filter
	vhsBP2 = PImage.alpha_composite(vhsBP1,nLoad)
	vhsAr = vhsAP2.resize([1440,1080],resample=PImage.LANCZOS).convert("L")
	vhsBr = vhsBP2.resize([1440,1080],resample=PImage.LANCZOS).convert("L")
	VHSP1 = vhsLTST.resize([1440,1080],resample=PImage.LANCZOS).convert("L") # resize back to original [USE BILINEAR]
#	print(x)
#	print(y)
	vhsP2 = PImage.merge("LAB",(VHSP1,vhsAr,vhsBr))
	vhsP3 = vhsP2.resize([x,y],resample=PImage.LANCZOS)
	conver2 = PImageCms.buildTransformFromOpenProfiles(labP,srgbP,"LAB","RGB")
	vhsFin = PImageCms.applyTransform(vhsP3,conver2)
	vhsFin.save('vhs.png')
	vhsAr.save('testA.png')
	vhsBr.save('testB.png')
	VHSP1.save('testL.png')
	# combine L and AB
	# save"""
	
