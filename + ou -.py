import random # importation de la bibliothèque

nombreJoueur = 0  # Créations des variables
nombreMystere = random.randint(1,100)
condition = True

while condition: # Boucle du test
	nombreJoueur = int(input("Entrez un nombre : ")) # On récupère la valeur de l'utilisateur

	if nombreJoueur > nombreMystere: # On teste comment est le nb Joueur comparé au nb Mystere
		print("Le nombre Mystere est plus petit.")
	elif nombreJoueur < nombreMystere:
		print("Le nombre Mystere est plus grand.")
	elif nombreJoueur == nombreMystere:
		print("Gagné !")
		condition = False
	
