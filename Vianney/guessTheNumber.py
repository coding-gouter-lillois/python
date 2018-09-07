#Importation du fichier qui permet d'avoir des nombres aléatoirs
import random

#La variable 'number' obtient une valeur comprise entre 1 & 10
number = random.randint(1, 10)
print(number)

#???
tries = 1

#Demande du nom du joueur
username = input("Hello, what's your name?")

#Dit bonjour au joueur
print("Hello", username + ".")

#Demande au joueur si il veut jouer (J'espère que oui, c'est le but du programme ^^")
question = input("Do you want to play a game? [Y/N]")

#Si la réponse est 'n' (No)
if question == "n":
    print("Oh... Ok ;(")

#Si la réponse est 'y' (Yes)
if question == "y":
    print("I'm thinking of a number between 1 and 10")
    guess = int(input("Have a guess :"))

#Boucle infinie qui teste la réponse donnée par le joueur
while 1:
    if guess == number:
        print("Well done!")
        print("You found in", tries, "tries!")
    else:
        tries = tries + 1
        if guess >= number:
            int(input("Guess lower :"))
        else:
            int(input("Guess highter :"))
