import random

#initialisation des listes#
boules_principale = []
for i in range(1,51):
  boules_principale.append(i)
print(boules_principale)

boules_etoile = []
for i in range(1,13):
  boules_etoile.append(i)
print(boules_etoile)

#melange des listes#
for i in range(50):
	random.shuffle(boules_principale)

for i in range(12):
	random.shuffle(boules_etoile)

#premier tirage#
tirage_principal = []
tirage_principal = random.sample(boules_principale,5)

#second tirage#
tirage_etoile = []
tirage_etoile = random.sample(boules_etoile,2)

#trie des numeros#
tirage_principal.sort()
tirage_etoile.sort()

#affichage des numeros tirés#
print("Tirage principale : ",tirage_principal)
print("Tirage etoile :", tirage_etoile)

#ajoute du texte
