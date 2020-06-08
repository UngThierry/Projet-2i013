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
    coup = game.getCoupsValides(jeu)
    return coup[0]