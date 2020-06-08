#!/usr/bin/env python
# -*- coding: utf-8 -*-
import game
def initialiseJeu():
    #jeu:[plateau nat List[coup] List[coup] List[nat nat]]
    jeu = []
    plateau = [[4,4,4,4,4,4],
               [4,4,4,4,4,4]]
    jeu.append(plateau)
    jeu.append(1)
    jeu.append(None)
    jeu.append([])
    jeu.append([0,0])
    return jeu


def affiche(jeu):
    print("Coup joue = "+str(jeu[3][-1]))
    print("Scores = "+str(jeu[4][0])+","+str(jeu[4][1]))
    print("Plateau : ")
    print("           |  0  |  1  |  2  |  3  |  4  |  5  |")   
    print("         -----------------------------------------")
    for i in range(2):
        print("         "+str(i)+" |"+"  "+str(game.getCaseVal(jeu,i,0))+"  |"+"  "+str(game.getCaseVal(jeu,i,1))+"  |"+"  "+str(game.getCaseVal(jeu,i,2))+"  |"+"  "+str(game.getCaseVal(jeu,i,3))+"  |"+"  "+str(game.getCaseVal(jeu,i,4))+"  |"+"  "+str(game.getCaseVal(jeu,i,5))+"  |")
        print("         -----------------------------------------")
        game.changeJoueur(jeu)
    print("         Joueur "+str(game.getJoueur(jeu))+" a vous de jouer \n")

def advaffame(jeu):
    adv = jeu[1]%2+1
    return (sum(jeu[0][adv-1]) == 0)

def getCoupsValides(jeu):
    a = advaffame(jeu)
    j = game.getJoueur(jeu)
    return [(j-1,i) for i in range(6) if game.getCaseVal(jeu,j-1,i)> 0 and ((not a) or nourrit(jeu,(j-1,i)))]
    
def nourrit(jeu,coup):
    j = game.getJoueur(jeu)
    if (j==1):
        return coup[1] < game.getCaseVal(jeu,coup[0],coup[1])
    else:
        return game.getCaseVal(jeu,coup[0],coup[1]) > (5-coup[1])
        
def distribue(jeu,case):
    v = game.getCaseVal(jeu,case[0],case[1])
    jeu[0][case[0]][case[1]] = 0
    nc = case
    while v > 0:
        nc = nextCase(nc[0],nc[1])
        if (not nc == case):
            jeu[0][nc[0]][nc[1]]+=1
            v-=1 
    return nc
    
def nextCase(l,c,horaire=False):
    if horaire:
        if (c == 5 and l == 0):
            return(1,c)
        if (c == 0 and l == 1):
            return(0,c)
        if (l == 0):
            return(l,c+1)
        return(l,c-1)
    else:
        if (c == 5 and l == 1):
            return(0,c)
        if (c == 0 and l == 0):
            return(1,c)
        if (l == 0):
            return(l,c-1)
        return(l,c+1)
    
def joueCoup(jeu,coup):
    l,c = distribue(jeu,coup)
    j = game.getJoueur(jeu)
    save = game.getCopieJeu(jeu)
    v = game.getCaseVal(jeu,l,c)
    while (l == (j%2)) and ((v == 2) or (v == 3)):
        jeu[0][l][c] = 0
        jeu[-1][j-1]+=v
        l,c = nextCase(l,c,True)
        v = game.getCaseVal(jeu,l,c)
        if advaffame(jeu):
            jeu[0] = save[0]
            jeu[-1] = save[-1]
    game.changeJoueur(jeu)
    jeu[2] = None
    jeu[3].append(coup)
        