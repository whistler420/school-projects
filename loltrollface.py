import matplotlib.pyplot as plt
import csv
cssv = open('/home/whistler/Documents/series.csv','r')
Rr = csv.reader(cssv)
#name2 = []
name = []
U = []
#l1v1 = []
#OG = []
for row in Rr:
#	name2 += []
	name += [row[0]]
	U += [row[1]]
#	l1v1 += [row[2]]
#	OG += [row[3]]
#y = [0, 1, 5, 10, 50, 100]
plt.bar(name,U)
#plt.ylabel(name)
plt.show()
