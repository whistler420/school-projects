#whistler's dumb calculator thing
#started 2019/10/03, "finished" 2019/10/15, and actually finished 2020/08/13
#because my power's out and there's nothing to do
from calcStr import *
import sys, time, os
#13 spaces in window
calcAns = 0
slpTime = 0.50
def drawCalc():
	global calcAns2
	ansLen = len(str(calcAns))
	if ansLen >= 11:
		ansLen = 11
	ansLenWrk = 13 - ansLen
	calcAnsWrk = " " * ansLenWrk
	calcAns2 = calcAnsWrk + str(calcAns)
	print(calcTop + calcScr + f"| |{calcAns2}| |\n" + calcScr + calcBlank + calcButnR0 + calcBlank + calcButnR1 + calcBlank + calcButnR2 + calcBlank + calcButnR3 + calcBlank + calcTop)
def prgClose():
	print(calcClose)
	time.sleep(slpTime)
	os.system('clear')
	sys.exit()
def outputHeader():
	os.system('clear')
	print(valueOutput + empty)
def addHeader():
	os.system('clear')
	print(valueA + empty)
def subHeader():
	os.system('clear')
	print(valueS + empty)
def multHeader():
	os.system('clear')
	print(valueM + empty)
def divHeader():
	os.system('clear')
	print(valueD + empty)
def errHeader():
	os.system('clear')
	print(valueE + empty)

brek = 0
while brek == 0:
	try:
		os.system('clear')
		print(menuCalc2)
		sel = int(input(op))
		if sel >= 2:
			brek += 1
			prgClose()
		elif sel == 1 or sel == 0:
			brek += 1
			os.system('clear')
			time.sleep(slpTime)
			print(menuCalc1)
			sel2 = int(input(op))
			time.sleep(slpTime)
			if sel2 == 4: #divison
				divHeader()
				var0 = float(input(calcVal1))
				time.sleep(slpTime)
				divHeader()
				var1 = float(input(calcVal2))
				time.sleep(slpTime)
				plswork = var0/var1
				calcAns = plswork
				os.system('clear')
				outputHeader()
				drawCalc()
			if sel2 <= 1: #addition
				addHeader()
				var0 = float(input(calcVal1))
				time.sleep(slpTime)
				addHeader()
				var1 = float(input(calcVal2))
				time.sleep(slpTime)
				plswork = var0 + var1
				calcAns = plswork
				os.system('clear')
				outputHeader()
				drawCalc()
			if sel2 == 2: #subtraction
				subHeader()
				var0 = float(input(calcVal1))
				time.sleep(slpTime)
				subHeader()
				var1 = float(input(calcVal2))
				time.sleep(slpTime)
				plswork = var0 - var1
				calcAns = plswork
				os.system('clear')
				outputHeader()
				drawCalc()
			if sel2 == 3: #mutiplication
				multHeader()
				var0 = float(input(calcVal1))
				time.sleep(slpTime)
				multHeader()
				var1 = float(input(calcVal2))
				time.sleep(slpTime)
				plswork = var0 * var1
				calcAns = plswork
				os.system('clear')
				outputHeader()
				drawCalc()
			if sel2 >= 5: #what the fuck did you do
				errHeader()
				print(error2)
	except ValueError:
		errHeader()
		print(error2)
	except KeyboardInterrupt:
		prgClose()
	except ZeroDivisionError:
		errHeader()
		print(divZeroError)
if calcAns >= 1:
	ansLen = len(str(calcAns))
	ansLenWrk = 13 - ansLen
	calcAnsWrk = " " * ansLenWrk
	calcAns2 = calcAnsWrk + str(calcAns)
