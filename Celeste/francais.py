#!/usr/bin/env python
# -*- coding: utf-8 -*-
def affiche_options():
    print ("\n 1 : Attribut du sujet")
    print (" 2 : COD")
    print (" 3 : COI")
    print (" 4 : COS")
    print (" 5 : epithete")
    print (" 6 : Complement du nom")
    print (" 7 : Complement circonstanciel")

def pose_question(bonne_reponse):
    dewale=True
    errors=0

    while dewale:
        affiche_options()
        reponse = raw_input ()

        if ( reponse == bonne_reponse):
            print "\033[96mBravo !\033[0m"
            dewale=False
        else:
            errors += 1
            if errors > 2:
                print "\033[91mGros(se) naze, vas apprendre ta leçon !\033[0m"
            else:
                print "\033[93mEssaye encore !\033[0m"

def affiche_phrase(phrase):
    print "\n\033[32m" + phrase + "\033[0m"

print ("==================================")
print ("   Bienvenu dans ton évaluation")
print ("==================================")


affiche_phrase ("Q1 : Le petit poucet est un enfant")
print ("Quel est la fonction de 'petit' dans la phrase précédente ?")
pose_question("1")

affiche_phrase ("Q2 : Le petit poucet guide ses frères")
print ("Quel est la fonction de 'ses frères' dans la phrase précédente ?")
pose_question("2")

affiche_phrase ("Q3 : Il parle à l'ogre")
print ("Quel est la fonction de \"à l'ogre\" dans la phrase précédente ?")
pose_question("3")

affiche_phrase ("Q4 : Il tend un piège à l'ogre")
print ("Quel est la fonction de \"à l'ogre\" dans la phrase précédente ?")
pose_question("4")

affiche_phrase ("Q5 : Le petit poucet est malin")
print ("Quel est la fonction de \"est malin\" dans la phrase précédente ?")
pose_question("5")


affiche_phrase ("Q6 : Le petit poucet a enfile les botte du geant")
print ("Quel est la fonction de \"du geant\" dans la phrase précédente ?")
pose_question("6")

affiche_phrase ("Q7 : Le lendemain,Cendrillon epousa le prince dans son chateau")
print ("Quel est la fonction de \"dans son chateau\" dans la phrase précédente ?")
pose_question("7")
