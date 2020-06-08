#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce
import game

def initialiseJeu():
    #jeu:[plateau nat List[coup] List[coup] List[nat nat]]
    jeu = []
    plateau = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 2, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]
    jeu.append(plateau)
    jeu.append(1)
    jeu.append(None) #None
    jeu.append([]) #[]
    jeu.append([2,2])
    return jeu

def affiche(jeu):
    print("Coup joue = "+str(jeu[3][-1]))
    print("Scores = "+str(jeu[4][0])+","+str(jeu[4][1]))
    print("Plateau : ")
    print("           |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |")   
    print("         -----------------------------------------------------")
    for i in range(8):
        print("         "+str(i)+" |"+"  "+str(game.getCaseVal(jeu,i,0))+"  |"+"  "+str(game.getCaseVal(jeu,i,1))+"  |"+"  "+str(game.getCaseVal(jeu,i,2))+"  |"+"  "+str(game.getCaseVal(jeu,i,3))+"  |"+"  "+str(game.getCaseVal(jeu,i,4))+"  |"+"  "+str(game.getCaseVal(jeu,i,5))+"  |"+"  "+str(game.getCaseVal(jeu,i,6))+"  |"+"  "+str(game.getCaseVal(jeu,i,7))+"  |")
        print("         -----------------------------------------------------")
        game.changeJoueur(jeu)
    print("         Joueur "+str(game.getJoueur(jeu))+" a vous de jouer \n")

def coups(jeu):
    adv = jeu[1]%2+1
    s = [entourageVide(jeu,l,c) for l in range(8) for c in range(8) if jeu[0][l][c] == adv]
    if s != []:
        s = reduce(lambda a,b:a|b,s)
    return s

def entourageVide(jeu,l,c):
    return{(l+i,c+j) for i in [-1,0,1] for j in [-1,0,1] if (c+j <= 7) and (c-j >= 0) and (l+i <= 7) and (l-i >= 0) and jeu[0][l+i][c+j] == 0}

def getCoupsValides(jeu):
    coup = coups(jeu)
    return [x for x in coup if (len(getEncadrements(jeu,x,False)))>0]

def getEncadrements(jeu,coup,all = True):
    ret = []
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i == 0 and j == 0:
                continue
            if checkEncadrementDirection(jeu,coup,i,j):
                ret.append((i,j))
                if not all:
                    break
    return ret

def checkEncadrementDirection(jeu,coup,i,j):
    l,c = coup
    while True:
        l+= i 
        c+= j
        if (l>7) or (l<0) or (c>7) or(c<0):
            return False
        if jeu[0][l][c] == 0:
            return False
        if jeu[0][l][c] == jeu[1]:
            return True

def joueCoup(jeu,coup):
    jeu[0][coup[0]][coup[1]] == jeu[1]
    if(jeu[1] == 1):
        jeu[4][0] += 1
    else:
        jeu[4][1] += 1
    d = getEncadrements(jeu,coup)
    for x in d:
        retournePions(jeu,coup,x)
    jeu[3].append(coup)
    jeu[2] = None
    jeu[1] = jeu[1]%2+1

def retournePions(jeu,coup,encadrement):
    jeu[0][coup[0]][coup[1]] = jeu[1]
    coups = [coup[0]+encadrement[0],coup[1]+encadrement[1]]
    while jeu[0][coups[0]][coups[1]] == jeu[1]%2+1:
        jeu[0][coups[0]][coups[1]] = jeu[1]
        jeu[4][jeu[1]-1] +=1
        jeu[4][jeu[1]%2] -=1
        coups = [coups[0]+encadrement[0],coups[1]+encadrement[1]]
            
