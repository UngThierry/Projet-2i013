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
    coup = (int(x),int(y))
    while ((coup[0] < 0 or coup[0] > 7) or (coup[1] < 0 or coup[1] > 7) and (jeu[0][coup[0]][coup[1]] != 0)):
        print("\nVeuillez saisir une case avec x entre 0 et 7 et y entre 0 et 7")
        x = input('Veuillez saisir le x : ')
        y = input('veuillez saisir le y : ')
        coup = (int(x),int(y))
        if (coup[0] > 0 and coup[0] < 7) and (coup[1] > 0 and coup[1] < 7):
            break
    return coup
