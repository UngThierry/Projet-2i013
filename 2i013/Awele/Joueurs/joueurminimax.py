#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append("../..")
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
import game
pmax = 3

coefs=[5,-4,4,1,1]





def dot(L1,L2):
    return sum(x*y for x,y in zip(L1,L2))





def saisieCoup(jeu):

    """ jeu -> coup
        Retourne un coup a jouer
    """
    global moi
    moi=game.getJoueur(jeu)
    global adv
    adv = moi % 2 +1

    global tour

    coups=game.getCoupsValides(jeu)





    return decision(jeu,coups)[0]











def decision(jeu,coups):
    """ jeu*coups-> [coup, scoremax]
        retourne le coup et le score qui donne un plus grand score
    """


    #copie=game.getCopieJeu(jeu)

    #game.joueCoup(copie,coups[0])
    meill_coup=coups[0]

    scoremax =  float('-inf')
    for cp in coups:
        copie=game.getCopieJeu(jeu)
        game.joueCoup(copie,cp)
        s = estimation(copie,False)

        if ( s > scoremax):
            scoremax = s
            meill_coup=cp
    res=[]
    res.append(meill_coup)
    res.append(scoremax)

    return res




def estimation(jeu,me,p=1):

    global pmax



    if p==pmax or game.finJeu(jeu):
        return evaluation(jeu)

    vmax = None

    coups= game.getCoupsValides(jeu)
    for cp in coups:
        copie=game.getCopieJeu(jeu)
        game.joueCoup(copie,cp)

        if me:

            v = estimation(copie,False,p+1)

            if vmax is None:

                vmax =v



            if (vmax<v):
                vmax =v

        else:

            v = estimation(copie,True,p+1)

            if vmax is None:

                vmax = v



            if (vmax>v):

                vmax=v


    return vmax




def evaluation(jeu):
    """Jeu*coup->double
       retourne le poids du coup passe en parametre a partir de la somme des coef
       et de differentes fonctions d'evaluation"""

    global moi

    if game.finJeu(jeu):
        return getFinDePartie(jeu,moi)

    else:

        score = [game.getScores(jeu)[moi -1],getCasesDes(jeu,moi),getCasesAv(jeu,moi),getNbGraines(jeu,moi),getPrises(jeu,moi)]

        return dot(coefs,score)

def getScore(jeu,joueur):
    """Jeu*int->int
       retourne le score d'un joueur"""
    return jeu[4][joueur-1]

def getCasesDes(jeu,joueur):
    """jeu*int->int
       retourne le max des cases successives valant 2 ou 3
       hypothese : comme avoir des cases faibles est desavantageux, ce coef sera negatif"""
    nb=0
    nbmax=0
    global moi
    if joueur==moi:
        for i in range(6):
            case=jeu[0][joueur-1][i]
            if case==0 or case == 1 or case == 2:
                nb+=1
            else:
                nbmax=max(nb,nbmax)
                nb=0
    nbmax=max(nb,nbmax)
    return nbmax

def getCasesAv(jeu,joueur):
    """jeu*int->int
       retourne le max des cases successives de l'adversaire valant 2 ou 3
       hypothese : comme avoir des cases faibles est desavantageux pour l'adversaire, ce coef sera positif"""
    global adv
    nb=0
    nbmax=0
    if joueur==adv:
        for i in range(6):
            case=jeu[0][joueur%2][i]
            if case==0 or case == 1 or case == 2:
                nb+=1
            else:
                nbmax=max(nb,nbmax)
                nb=0
    nbmax=max(nb,nbmax)
    return nbmax

def getNbGraines(jeu,joueur):
    """Jeu*int->int
       retourne la difference de graines entre le joueur et l'adversaire"""
    nb_joueur=0
    nb_adversaire=0

    global moi
    adversaire = moi %2 +1

    for i in range(6):
        nb_joueur+=jeu[0][joueur-1][i]
        nb_adversaire+=jeu[0][adversaire-1][i]

    return nb_joueur-nb_adversaire

def getPrises(jeu,joueur):
    """Jeu*int->int
       retourne les differentes autres possibilites de prises"""
    global moi
    cases=[0,0,0,0,0,0]
    if joueur==moi :
        for i in range(6) :
            valeur=jeu[0][joueur-1][i]
            nbG=((valeur//12)+valeur)%12
            if joueur-1 == 0 :
                nbG-=i
            else:
                nbG-=(5-i)
            if nbG>=0 and nbG<=6 :
                cases[nbG-1]+=1
    res = 0
    for e in cases :
        if e>0:
            res+=1
    return res


def getFinDePartie(jeu,joueur):
    """Jeu*int->int
       retourne la valeur de retour de fin de partie (1=gagne -1=perdu 0=en cours)"""
    global moi
    if game.finJeu(jeu):
        if game.getGagnant(jeu)==moi :
            return 1
        else :
            return -1

    return 0
