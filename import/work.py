import vhs
import PIL.Image as PImage
import PIL.ImageCms as PImageCms
from tkinter import filedialog as File #shamelessly stolen from test.py BECAUSE IT JUST WORKS GOGAMMIT
from tkinter import *
def vhsConvert():
	srgbP = PImageCms.createProfile("sRGB")
	labP = PImageCms.createProfile("LAB")
	conver = PImageCms.buildTransformFromOpenProfiles(srgbP,labP,"RGB","LAB")
	VHS = PImageCms.applyTransform(vhs.img,conver) # convert to LAB color
	L,a,b = VHS.split()  # split L and AB into separate files
	vhsLP1 = L.resize([333,480],resample=PImage.BICUBIC).convert("RGBA") # resize L
	vhsAP1 = a.resize([40,480],resample=PImage.BICUBIC).convert("RGBA") 
	vhsBP1 = b.resize([40,480],resample=PImage.BICUBIC).convert("RGBA") # resize AB
	nLoad = PImage.open("/home/whistler/import/noise.png").convert("RGBA")
	nLoad2 = PImage.open("/home/whistler/import/noiseBig.png").convert("RGBA")
	vhsLTST = PImage.alpha_composite(vhsLP1,nLoad2)
	vhsAP2 = PImage.alpha_composite(vhsAP1,nLoad) # add noise filter
	vhsBP2 = PImage.alpha_composite(vhsBP1,nLoad)
	vhsAr = vhsAP2.resize([x,y],resample=PImage.ANTIALIAS).convert("L")
	vhsBr = vhsBP2.resize([x,y],resample=PImage.ANTIALIAS).convert("L")
	VHSP1 = vhsLP1.resize([x,y],resample=PImage.ANTIALIAS).convert("L") # resize back to original [USE BILINEAR]
#	print(x)
#	print(y)
	vhsP2 = PImage.merge("LAB",(VHSP1,vhsAr,vhsBr))
	conver2 = PImageCms.buildTransformFromOpenProfiles(labP,srgbP,"LAB","RGB")
	vhsFin = PImageCms.applyTransform(vhsP2,conver2)

