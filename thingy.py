import PIL.Image
red = 0
grn = 0
blu = 0
redStr = "================\ \nRed Pixels: "
blueStr = "Blue Pixels: "
greenStr = "Green Pixels: "
red1 = "Red: "
grn1 = "Green: "
blu1 = "Blue: "
newLine = "\n"

openImg = "/home/whistler/RGB.png" # replace later
#openImg = "/home/whistler/ma mario.png" # replace later
img = PIL.Image.open(openImg)
openFile = open("/home/whistler/thingy/colors.txt","w+")
#print(img.mode)
for y in range(img.size[1]):
	for x in range(img.size[0]):
		c = img.load()
		r = c[x,y][0]
		g = c[x,y][1]
		b = c[x,y][2]
		c[x,y] = (r,g,b)
		openFile.write(red1+str(r)+newLine)
		openFile.write(grn1+str(g)+newLine)
		openFile.write(blu1+str(b)+newLine)
		if r > 99:
			red += 1
		if g > 99:
			grn += 1
		if b > 99:
			blu += 1
#		print(red)
openFile.write(redStr+str(red)+newLine+greenStr+str(grn)+newLine+blueStr+str(blu))
openFile.close
