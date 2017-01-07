#!/usr/bin/env python
# -*- coding: utf-8 -*-

operation = raw_input("Quelle opération ? ")

if (operation == "+") :
    thomas = raw_input("Quel est le premier nombre ? ")
    anne = raw_input("Quel est le second nombre ? ")
    celeste = int(thomas) + int(anne)
    print ("La somme est : %d" % celeste)

if (operation == "*") :
    papa = raw_input("Quel est le premier nombre à multiplier ?")
    maman = raw_input("Quel est le second nombre a multiplier ?")
    oscar = int(papa) * int(maman)
    print ("le resulta est : %d" % oscar)

if (operation == "-") :
    tata = raw_input("Quel est le premier nombre à soustrere ?")
    mikael = raw_input("Quel est le second nombre à soustrere ?")
    pleure = int(tata) - int(mikael)
    print ("le resulta est : %d" % pleure)

if (operation == "/") :
   tonton = raw_input("Quel est le premier nombre à diviser ?")
   elodie = raw_input("Quel est le second nombre à diviser ?")
   mort = int(tonton) / int(elodie)
   enterment =int(tonton) % int(elodie)
   print ("le quosient est : %d et le reste est : %d" % (mort, enterment))
