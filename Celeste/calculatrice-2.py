#!/usr/bin/env python
# -*- coding: utf-8 -*-

operation = raw_input("Quelle opération ? ")
gauche = raw_input("Quel est le premier nombre ? ")
droite = raw_input("Quel est le second nombre ? ")

if (operation == "+") :
    resulta = int(gauche) + int(droite)
    message = "La somme est : %d" % resulta

if (operation == "*") :
    resulta = int(gauche) * int(droite)
    message = "le resulta est : %d" % resulta

if (operation == "-") :
    resulta = int(gauche) - int(droite)
    message = "le resulta est : %d" % resulta

if (operation == "/") :
   resulta = int(gauche) / int(droite)
   reste =int(gauche) % int(droite)
   message = "le quosient est : %d et le reste est : %d" % (resulta, reste)

print(message)
