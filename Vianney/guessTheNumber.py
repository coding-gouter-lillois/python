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

#Si la réponse est 'n' (No)
if question == "n":
    print("Oh... Ok ;(")

#Si la réponse est 'y' (Yes)
if question == "y":
    print("I'm thinking of a number between 1 and 10")
    guess = int(input("Have a guess :"))

#Boucle infinie
while 1:
    if guess == number: #Si le nombre donné par le joueur est le bon
        print("Well done!")
        print("You found in", tries, "tries!")
        break
    else: #Sinon ; on ajoute 1 au nombre d'essais, et on donne une indication pour faciliter la recherche du joueur
        tries = tries + 1
        if guess < number:
            int(input("Guess lower :"))    
        if guess < number:
            int(input("Guess highter :"))
