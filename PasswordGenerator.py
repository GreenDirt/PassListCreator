#coding: utf-8
import json
print("\t-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("\tPasswordGenerator V.prealpha")
print("\t_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n\n")

nomImportant = []
date = []

prenom = input("Entrez le prénom de votre cible : ")
nom = input("Entrez le nom de votre cible : ")

i = 0
val = 1
while val:
	print("Nom : " + nom + " | Prénom : " + prenom + "\n")
	info = input("Souhaitez vous  ajouter des informations ?\t 1 : date | 2 : autre(nom, lieu...) | 3 : non\n>")
	if info == '1':
		date.insert(i, input("Entrez votre date : "))
	elif info == '2':
		nomImportant.insert(i, input("Entrez votre autre information : "))
	else:
		val = 0
	i += 1
n = 1
while n:
	linkFile = input("Entrez le chemin complet où stocker votre fichier : ")
	if linkFile[0] != '/':
		print("Veuillez entrer une valeur correcte.")
	elif linkFile[-1] != '/':
		linkFile = linkFile + '/'
		n = 0
	else:
		n = 0

print("----------------------")
print("Création du fichier...")
print("----------------------")

liste = open("passlist.json", "r")				#Ouverture de la liste par default de mots de passe en lecture

rlist = liste.readlines()						#enregistrement des mdp par default dans une liste
i = 1600


n = 0
while n < len(date):
	if len(date) and len(nomImportant):
		if date[n] == '':
			date[n] = ''
		if nomImportant[n] == '':
			nomImportant[n] == ''

		rlist.append(date[n] + nomImportant[n] + '\n')
		rlist.append(nomImportant[n] + date[n] + '\n')
		rlist.append(nomImportant[n] + "1234" + date[n] + '\n')
		rlist.append(date[n] + nomImportant[n] + '\n')
		rlist.append(nomImportant[n] + date[n] + '\n')
		rlist.append(nomImportant[n] + "1234" + date[n] + '\n')
	if len(date):
		rlist.append(date[n] + nom + '\n')
		rlist.append(nom + date[n] + '\n')
		rlist.append(nom + "1234" + date[n] + '\n')
		rlist.append(date[n] + prenom + '\n')
		rlist.append(prenom + date[n] + '\n')
		rlist.append(prenom + "1234" + date[n] + '\n')
		rlist.append(date[n])
	n += 1

n = 0
while n < len(nomImportant):	
	if len(nomImportant):
		rlist.append(nomImportant[n] + nom + '\n')
		rlist.append(nom + nomImportant[n] + '\n')
		rlist.append(nom + "1234" + nomImportant[n] + '\n')
		rlist.append(nomImportant[n] + prenom + '\n')
		rlist.append(prenom + nomImportant[n] + '\n')
		rlist.append(prenom + "1234" + nomImportant[n] + '\n')
		rlist.append(nomImportant[n])
	n += 1

rlist.append(nom + "123\n")
rlist.append(nom + "1234\n")
rlist.append(nom + "12345\n")
rlist.append(prenom + "123\n")
rlist.append(prenom + "1234\n")
rlist.append(prenom + "12345\n")
rlist.append(prenom + "123456\n")

while i <= 2500:
	rlist.append(nom + "%i\n"%i)
	rlist.append(prenom + "%i\n"%i)
	b = 0
	c = 0
	while b <= 100:
		rlist.append(prenom + '0' + str(b) + '0' + str(c) + str(i) + '\n')
		rlist.append(nomImportant[n-1] + '0' + str(b) + '0' + str(c) + str(i) + '\n')
		b += 1
		rlist.append(prenom + '0' + str(b) + '0' + str(c) + str(i) + '\n')
		rlist.append(nomImportant[n-1] + '0' + str(b) + '0' + str(c) + str(i) + '\n')
		c += 1
		rlist.append(prenom + '0' + str(b) + '0' + str(c) + str(i) + '\n')
		rlist.append(nomImportant[n-1] + '0' + str(b) + '0' + str(c) + str(i) + '\n')
	i += 1	

rlist.append('')								#Derniere entree de la liste
print(rlist)

passliste = open(linkFile + "passlistUser.json", "w")
i = 0
while rlist[i] != '':	
	passliste.write(rlist[i])
	i += 1

liste.close()
passliste.close()

print("----------------------")
print(" Création réussite !")
print("----------------------")
print("Votre fichier s'appelle PasslistUser.json et se trouve dans le répertoire %s, il contient "% (str(linkFile)) + str(len(rlist)) + " entrées.")