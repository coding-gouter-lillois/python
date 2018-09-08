#Importation du fichier qui permet d'avoir des nombres aléatoirs
import random

#La variable 'number' obtient une valeur comprise entre 1 & 10
number = random.randint(1, 10)
print(number)

#Variable du nombre d'essais
tries = 1

#Demande du nom du joueur
username = input("Hello, what's your name?")

#Dit bonjour au joueur
print("Hello", username + ".")

#Demande au joueur si il veut jouer (J'espère que oui, c'est le but du programme ^^")
question = input("Do you want to play a game? [Y/N]")
if question == "n":
	print("Oh... Ok ;(")
else:
	while 1:
		print("I'm thinking of a number between 1 and 10")
		guess = int(input("Have a guess :"))

#Boucle infinie
	while guess != number:
		tries = tries + 1
		if guess < number:
			guess = int(input("Guess highter :"))
		if guess > number:
			guess = int(input("Guess lower :"))
	else:
		print("Well done")

