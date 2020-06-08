#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")    

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    x = input('Veuillez saisir le x : ')
    y = input('veuillez saisir le y : ')
    coup = [int(x),int(y)]
    while ((coup[0] < 0 or coup[0] > 1) or (coup[1] < 0 or coup[1] > 5)):
        print("\nVeuillez saisir une case avec x entre 0 et 5 et y entre 0 et 2")
        x = input('Veuillez saisir le x : ')
        y = input('veuillez saisir le y : ')
        coup = (int(x),int(y))
        if (coup[0] >= 0 and coup[0] <= 1) and (coup[1] >= 0 and coup[1] <= 5):
            break
    return coup
