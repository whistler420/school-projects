from tkinter import *
def reduce(c):
	global outList
	outList = [0,0,0]
	outList[0] = c[0]//3
	outList[1] = c[1]//3
	outList[2] = c[2]//3
	return outList
broke = 1
try:
	c0 = int(input("Please give me a value: "))
	c1 = int(input("Now give me another: "))
	c2 = int(input("And another: "))
	col1 = (c0,c1,c2)
	reduce(col1)
	print(outList)
	broke <= 1
except ValueError:
	print("pls I said a value or integer")
	broke = 1
root = Tk()
root.mainloop()
