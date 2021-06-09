from tkinter import *
from PIL import Image,ImageTk
startTk = Tk()
winRes = "420x690"
startTk.resizable(False,False)
startTk.geometry(winRes)
def work():
	L2 = Label(startTk)
	L2.img = PhotoImage(file="/home/whistler/import/youvebeengn0med.png")
	L2.config(image=L2.img)
	L2.pack()
	b1.pack_forget()	
def something():
	b1.config(text="do it again lol",command=work)
	L1.pack_forget()
L1 = Label(startTk, text="funny joke")
L1.pack()
b1 = Button(startTk,text="click me for a funnier joke",command=something)
b1.pack()
startTk.mainloop()
