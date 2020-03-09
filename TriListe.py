import random
import time

maxVal = 100
nVal = 100
listeNombres = sorted(random.choices(range(maxVal), k=nVal), reverse = True)
print(listeNombres)

def triSelection(L:list) -> list:
	for j in range(0, len(L) -1):
		mini = j 
		for i in range(j+1, len(L)):
			if L[i] < L[mini]: mini = i  
		temp = L[j]
		L[j] = L[mini] 
		L[mini] = temp
		print(j, L)
	return L
	
	
def triInsertion(L:list) -> list:
	n = len(L)
	for i in range(n):
		valeurTraitee = L[i]
		j = i-1
		compteur += 1
		while j >= 0 and valeurTraitee < L[j]:
			L[j+1] = L[j]
			j = j-1
		L[j+1] = valeurTraitee
	return compteur

print(listeNombres)
listeNombresTriee = triInsertion(listeNombres)
print(listeNombresTriee)

nVal = [10**i for i in rnge(1, 4)]
maxVal = 100000
tableau = []
for n in range(3):
	listeLocal = []
for i in nVal:
	if(n == 0): listeNombres = random.choices(range(maxVal), k = i)
	if(n == 1): listeNombres = sorted(random.choices(range(maxVal), k = i)
	if(n == 2): listeNombres = sorted(random.choices(range(maxVal), k = i, reverse = True)
	t1 = time.time()
	triInsertion(listeNombres)
	t2 =time.time()
	listeLocal.append(t2-t1)
	tableau.append(listeLocal)

for ligne in tableau:
	print(ligne)
	
