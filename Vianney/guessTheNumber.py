#Importation du fichier qui permet d'avoir des nombres aléatoirs
import random

#Demande du nom du joueur
username = input("Hello, what's your name?")

#Dit bonjour au joueur
print("Hello", username + ".")

#Demande au joueur si il veut jouer (J'espère que oui, c'est le but du programme ^^")
question = input("Do you want to play a game? [Y/N]")
if question == "n":
    print("Oh... Ok ;(")

#Si la réponse est 'y' (Yes)
if question == "y":
    while 1:
        #La variable 'number' obtient une valeur comprise entre 1 & 10
        number = random.randint(1, 10)

        #Variable du nombre d'essais
        tries = 1
        
        #Annonce du début du jeu
        print("\nI'm thinking of a number between 1 and 10")
        guess = int(input("Have a guess :"))

        #Boucle infinie
        while guess != number:
            tries = tries + 1
            if guess < number:
                guess = int(input("Guess highter :"))
            if guess > number:
                guess = int(input("Guess lower :"))
        else:
            print("Well done", username, "!")
            if tries == 1:
                print("Wow... How lucky you are!")
            else:
                if tries < 5:
                    print("Nice! You won in", tries, "tries!\n\n\n")
                if tries > 5:
                    print("Well... You'll better do than", tries, "next time!\n\n\n")
