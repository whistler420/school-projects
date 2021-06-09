import time
f = open('bee sex.txt','r')
data = f.readlines()
for revenge in data:
	print(revenge.strip())
	time.sleep(1)
f.close()
