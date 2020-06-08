#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append("../..")
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
import game

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    #coup:[nat nat]
    for x in range(8):
        for y in range(8):
            coup = (x,y)
            if game.coupValide(jeu,coup):
                return coup
            
    #coups = game.getCoupsValides(jeu)
    #return coups[0]