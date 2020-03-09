import random
import time

tProg = time.time()
maxVal = 200
nVal = 100
listeNombres = sorted(random.choices(range(maxVal), k=nVal))
print(listeNombres)

#def rechercheNaive(L: list, elt: int)-> int:
	#for i in range(len(L)):
		#print("position ",i, " valeur ",L[i],elt)
		#if elt == L[i]:
			#return i
	#return -1


def rechercheDicho(L: list, elt: int)-> int:
	tr = False
	deb = 0
	fin = len(L)-1
	cnt = 0
	while tr == False and deb <= fin:
		mil = (deb+fin)//2
		print(deb, mil, fin, L[mil])
		if L[mil] == elt:
			tr == True
		else:
			if elt > L[mil]:
				deb = mil+1
			else:
				fin = mil-1
		cnt +=1
	return cnt

nVal = [2**i for i in range(1, 20)]
tDicho = []
tNaive = []
for i in nVal:
	#listeNombres = sorted(random.choices(range(maxVal), k=nVal))
	t1 = time.time()
	rechercheDicho(listeNombres, -1)
	t2 = time.time()
	tDicho.append(t2-t1)
	#t1 = time.time()
	#rechercheNaive(listeNombres, -1)
	#t2 = time.time()
	#tNaive.append(t2-t1)

print( nVal )
print( tDicho )
#print( tNaive )

tProg2 = time.time()
tempsProg = tProg2-tProg
