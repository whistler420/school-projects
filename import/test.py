import time, sys #TODO: add network support using response
import PIL.Image,PIL.ImageOps
from tkinter import filedialog as File
from tkinter import *
def loadColor():
	global c,r,g,b # actually make the variables work
	c = img.load()
	r = c[x,y][0]
	g = c[x,y][1]
	b = c[x,y][2]
startTk = Tk()
startTk.withdraw()
error = True
while error == True:
	usrIn = print('Please select an image file.')
	loadGui = filedialog.askopenfilename(initialdir = "/home",title = "IMAGE SELECTION",filetypes = (("All files","*.*"),("JPEG files","*.jpg *.JPEG"),("PNG files","*.png *.PNG"),("BMP files","*.bmp *.BMP")))
	error = False
	try:
		img = PIL.Image.open(loadGui)
	except AttributeError:
		sys.exit()
	except:
		print('Please try again.')
		error = True
print('Filename: ',img.filename)
#print('Extension (DEBUG): ',imgEx)
print('Format: ',img.format)
print('Mode: ',img.mode)
print('Size: ',img.size)
mod = input('Would you like to modify the image? \nY | N\n')
def prgExit():
	print('Now closing...')
	time.sleep(1)
	sys.exit()
if mod == 'Y' or mod == 'y':
	print("IMAGE MODIFICATION\n" + "------------" + "------------" + "\n1. Flip the image.\n" + "2. Resize the image.\n" + "3. Modify color values.\n" + "4. Add a border.\n" + "5. Close the program.")
	usrChoice = 0
	while usrChoice == 0:
		try:
			usrChoice = int(input("Please input a number now: "))
			if usrChoice >4:
				usrChoice -= 1
			elif usrChoice <1:
				usrChoice += 1
		except ValueError: 
			print('Please don\'t do that.')
			usrChoice == 0
	if usrChoice == 1:
		print("IMAGE MODIFICATION\n" + "------------" + "------------" + "\n1. Flip the image vertically","\n2. Flip the image horizontally","\n3. Mirror the image vertically","\n4. Mirror the image horizontally")
		_in = int(input("Select an option: "))
		if _in == 0 or _in == 1:
			flipV = img.transpose(PIL.Image.FLIP_TOP_BOTTOM)
			saveFunc = print('Where do you want the image to be saved?')
			saveGui = filedialog.askdirectory(initialdir = "/home",title = "DIRECTORY?")
			flipV.save(saveGui + "/edit." + img.format)
		elif _in == 2:
			flipH = img.transpose(PIL.Image.FLIP_LEFT_RIGHT)
			saveFunc = print('Where do you want the image to be saved?')
			saveGui = filedialog.askdirectory(initialdir = "/home",title = "DIRECTORY?")
			flipH.save(saveGui + "/edit." + img.format)
		elif _in == 3:
			#[IMAGE -> CROP -> COPY] -> FLIP -> PASTE -> SAVE
			mirY = int(img.size[1]/2)
			img.crop(box=[0,0,mirY,img.size[0]])
			img.copy()
			saveFunc = print('Where do you want the image to be saved?')
			saveGui = filedialog.askdirectory(initialdir = "/home",title = "DIRECTORY?")
			img.save(saveGui + "/debug." + img.format)
		elif _in >= 4:
			print("test")
	elif usrChoice == 2:
		if img.format == 'JPEG':
			img.format == 'jpg'
		x = 0
		y = 0
		while x == 0 or y == 0:
			try:
				y = int(input('Please input the new width: '))
				x = int(input('Please input the new height: '))
				print('Now working...')
				time.sleep(1.50)
				edit = img.resize([y,x]) #pillow is weird
				saveFunc = print('Where do you want the image to be saved?')
				saveGui = filedialog.askdirectory(initialdir = "/home",title = "DIRECTORY?")
				edit.save(saveGui + "/edit." + img.format)
				time.sleep(1.50)
				print('Done!')
			except:
				print('Sorry, an error occured.')
	elif usrChoice == 3:
		print("IMAGE MODIFICATION\n" + "------------" + "------------" + "\n1. Modify the Red channel" + "\n2. Modify the Blue channel" + "\n3. Modify the Green channel" + "\n4. Convert to Grayscale")
		in2 = int(input("select text: "))
		if in2 == 1 or in2 == 0:
			print("CHANNEL MODIFICATION\n" + "------------" + "------------" + "\n1. Swap with Blue" + "\n2. Swap with Green" + "\n3. Remove the Channel" + "\n4. Save the channel as an image")
			in3 = int(input("select test: "))
			if in3 == 0 or in3 == 1:
				for y in range(img.size[1]):
					for x in range(img.size[0]):
							loadColor()
							c[x,y] = (b, g, r)
				saveFunc = print('Where do you want the image to be saved?')
				saveGui = filedialog.askdirectory(initialdir = "/home",title = "DIRECTORY?")
				print(saveGui)
				img.save(saveGui + "/edit." + img.format)
				time.sleep(1.50)
				print('Done!')
			if in3 == 2:
				for y in range(img.size[1]):
					for x in range(img.size[0]):
						loadColor()
						c[x,y] = (g, r, b)
				saveFunc = print('Where do you want the image to be saved?')
				saveGui = filedialog.askdirectory(initialdir = "/home",title = "DIRECTORY?")
				img.save(saveGui + "/edit." + img.format)
				time.sleep(1.50)
				print('Done!')
			if in3 == 3:
				for y in range(img.size[1]):
					for x in range(img.size[0]):
						loadColor()
						c[x,y] = (0, g, b)
				saveFunc = print('Where do you want the image to be saved?')
				saveGui = filedialog.askdirectory(initialdir = "/home",title = "DIRECTORY?")
				img.save(saveGui + "/edit." + img.format)
				time.sleep(1.50)
				print('Done!')
			if in3 == 4:
				for y in range(img.size[1]):
					for x in range(img.size[0]):
						loadColor()
						c[x,y] = (r,0,0)
				saveFunc = print('Where do you want the image to be saved?')
				saveGui = filedialog.askdirectory(initialdir = "/home",title = "DIRECTORY?")
				img.save(saveGui + "/edit." + img.format)
				time.sleep(1.50)
				print('Done!')
		elif in2 == 2:
			print("CHANNEL MODIFICATION\n" + "------------" + "------------" + "\n1. Swap with Red" + "\n2. Swap with Green" + "\n3. Remove the Channel" + "\n4. Save the channel as an image")
			in3 = int(input("select test: "))
			if in3 == 0 or in3 == 1:
				for y in range(img.size[1]):
					for x in range(img.size[0]):
						loadColor()
						c[x,y] = (b, g, r)
				saveFunc = print('Where do you want the image to be saved?')
				saveGui = filedialog.askdirectory(initialdir = "/home",title = "DIRECTORY?")
				img.save(saveGui + "/edit." + img.format)
				time.sleep(1.50)
				print('Done!')
			if in3 == 2:
				for y in range(img.size[1]):
					for x in range(img.size[0]):
						loadColor()
						c[x,y] = (r, b, g)
				saveFunc = print('Where do you want the image to be saved?')
				saveGui = filedialog.askdirectory(initialdir = "/home",title = "DIRECTORY?")
				img.save(saveGui + "/edit." + img.format)
				time.sleep(1.50)
				print('Done!')
			if in3 == 3:
				for y in range(img.size[1]):
					for x in range(img.size[0]):
						loadColor()
						c[x,y] = (r, g, 0)
				saveFunc = print('Where do you want the image to be saved?')
				saveGui = filedialog.askdirectory(initialdir = "/home",title = "DIRECTORY?")
				img.save(saveGui + "/edit." + img.format)
				time.sleep(1.50)
				print('Done!')
			if in3 == 4:
				for y in range(img.size[1]):
					for x in range(img.size[0]):
						loadColor()
						c[x,y] = (0,0,b)
				saveFunc = print('Where do you want the image to be saved?')
				saveGui = filedialog.askdirectory(initialdir = "/home",title = "DIRECTORY?")
				img.save(saveGui + "/edit." + img.format)
				time.sleep(1.50)
				print('Done!')
		elif in2 == 3:
			print("CHANNEL MODIFICATION\n" + "------------" + "------------" + "\n1. Swap with Red" + "\n2. Swap with Blue" + "\n3. Remove the Channel" + "\n4. Save the channel as an image")
			in3 = int(input("select test: "))
			if in3 == 0 or in3 == 1:
				for y in range(img.size[1]):
					for x in range(img.size[0]):
						loadColor()
						c[x,y] = (g, r, b)
				saveFunc = print('Where do you want the image to be saved?')
				saveGui = filedialog.askdirectory(initialdir = "/home",title = "DIRECTORY?")
				img.save(saveGui + "/edit." + img.format)
				time.sleep(1.50)
				print('Done!')
			if in3 == 2:
				for y in range(img.size[1]):
					for x in range(img.size[0]):
						loadColor()
						c[x,y] = (r, b, g)
				saveFunc = print('Where do you want the image to be saved?')
				saveGui = filedialog.askdirectory(initialdir = "/home",title = "DIRECTORY?")
				img.save(saveGui + "/edit." + img.format)
				time.sleep(1.50)
				print('Done!')
			if in3 == 3:
				for y in range(img.size[1]):
					for x in range(img.size[0]):
						loadColor()
						c[x,y] = (r, 0, b)
				saveFunc = print('Where do you want the image to be saved?')
				saveGui = filedialog.askdirectory(initialdir = "/home",title = "DIRECTORY?")
				img.save(saveGui + "/edit." + img.format)
				time.sleep(1.50)
				print('Done!')
			if in3 == 4:
				for y in range(img.size[1]):
					for x in range(img.size[0]):
						loadColor()
						c[x,y] = (0,g,0)
				saveFunc = print('Where do you want the image to be saved?')
				saveGui = filedialog.askdirectory(initialdir = "/home",title = "DIRECTORY?")
				img.save(saveGui + "/edit." + img.format)
				time.sleep(1.50)
				print('Done!')
		elif in2 >= 4:
			c = img.convert("L")
			saveFunc = print('Where do you want the image to be saved?')
			saveGui = filedialog.askdirectory(initialdir = "/home",title = "DIRECTORY?")
			c.save(saveGui + "/edit." + img.format)
			time.sleep(1.50)
			print('Done!')
	elif usrChoice == 4:	#work on this later
		err1 = 0
		while err1 == 0:
			try:
				test = int(input('thing (px): '))
				print('red','blue','green','yellow')
				test2 = int(input('thing '))
				print('light','dark')
				light = int(input('thing '))
				print(test,test2,light)
				err1 += 1
			except:
				print('there was an error.')
	elif usrChoice >= 5:
		prgExit()
else:
	prgExit()
