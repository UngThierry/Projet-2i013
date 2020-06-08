#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
tmp= time.time()

import sys
sys.path.append("..")
import othello
sys.path.append("../..")
import game
game.game=othello
sys.path.append("./Joueurs")
import joueur_humain
import joueur_aleatoire
import joueur_premier_coup_valide
import joueur_horizon1_statique
import joueur_horizon1_dynamique
import joueurminimaxstatique
import joueurminimaxdynamique
import joueuralphabetastatique
import joueuralphabetadynamique
import joueurnegamax
import joueurnegascout
game.joueur1=joueur_aleatoire
game.joueur2=joueurminimaxdynamique
j1=0
j2=0
n1=0
n=100

for i in range(n):
    jeu=game.initialiseJeu()
    it=0
    jeu[3] = []
    jeu[3].append((None,None))
    game.affiche(jeu)
    while(it < 100) and (not game.finJeu(jeu)):
        jeu[2]=game.getCoupsValides(jeu)
        for coup in jeu[2]:
            if coup[0] == -1:
                coup = (7,coup[1])
            if coup[1] == -1:
                coup = (coup[0],7)
        if jeu[1] == 1:
            coup = game.joueur1.saisieCoup(jeu)
            while(game.coupValide(jeu,coup) == False):
                print("\nVeuillez resaisir une autre case valide : ")
                coup = game.joueur1.saisieCoup(jeu)
        else:
            coup = game.joueur2.saisieCoup(jeu)
            while(game.coupValide(jeu,coup) == False):
                print("\nVeuillez resaisir une autre case valide : ")
                coup = game.joueur2.saisieCoup(jeu)
        if coup[0] == -1:
            coup = (7,coup[1])
        if coup[1] == -1:
            coup = (coup[0],7)
        game.joueCoup(jeu,coup)
        game.affiche(jeu)
        if game.finJeu(jeu) == True:
            break
        it+=1
    print("Gagnant: "+str(game.getGagnant(jeu))+"\n")
    if(game.getGagnant(jeu)==1):
        j1+=1
    elif((game.getGagnant(jeu)==2)):
        j2+=1
    else:
        n1+=1

j1= 100*j1/n
j2= 100*j2/n
n1= 100*n1/n
print("Le joueur 1 a gagné : "+str(j1)+"% fois, le joueur 2 a gagné : "+str(j2)+"% fois et il y a eu : "+str(n1)+"% de matchs nuls")

tmp2 = time.time() - tmp

print("Temps d'exécution = ", tmp2)
