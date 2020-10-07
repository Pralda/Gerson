import random

nombreJoueur = 0
nombreMystere = random.randint(1,100)
condition = True
print(nombreMystere)
while condition:
	nombreJoueur = int(input("Entrez un nombre : "))

	if nombreJoueur > nombreMystere:
		print("Le nombre Mystere est plus petit.")
	elif nombreJoueur < nombreMystere:
		print("Le nombre Joueur est plus grand.")
	elif nombreJoueur == nombreMystere:
		print("Gagné !")
		condition = False
	else :
		print("Bug")	
