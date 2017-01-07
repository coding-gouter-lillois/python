#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, pygame
pygame.init()

ecran = pygame.display.set_mode(320,320)
ecran.fill(red)

balle = pygame.image.load("balle.jpg")
ballerect = balle.get_rect()
ecran.blit(balle, ballerect)
pygame.display.flip()
