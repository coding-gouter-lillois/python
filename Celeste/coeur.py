#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle

celeste = turtle.Turtle()
celeste.color('red', 'red')
celeste.pensize(1)

l=50
while l>0 :
    celeste.left(45)
    celeste.forward(l*1.414)
    celeste.right(45)
    celeste.forward(l)
    celeste.right(90)
    celeste.forward(l)
    celeste.right(45)
    celeste.forward(l*2*1.414)
    # Bas du coeur
    celeste.right(90)
    celeste.forward(l*2*1.414)
    celeste.right(45)
    celeste.forward(l)
    celeste.right(90)
    celeste.forward(l)
    celeste.right(45)
    celeste.forward(l*1.414)
    celeste.left(45)
    l = l-1

turtle.done()
