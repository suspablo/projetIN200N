#la fonction de dmouvement va se separer en plusieurs fonctions deja une pour tasser (enlever les zéros) et une pour fusionner les cases identiques
from grille import TAILLE

def tasser(ligne):
    nouvelle_ligne = []                  # on crée une liste vide
    for case in ligne:                   # on regarde chaque case
        if case != 0:                    # si la case n'est pas vide
            nouvelle_ligne.append(case)  # on la garde
    while len(nouvelle_ligne) < TAILLE:  # tant qu'il manque des cases
        nouvelle_ligne.append(0)         # on remet des zéros à droite
    return nouvelle_ligne

def fusionner(ligne): #fonction qui fusionne les cases identiques dans la 
    for i in range(TAILLE - 1):              # on regarde chaque case sauf la dernière
        if ligne[i] == ligne[i+1]:  
            ligne[i] = ligne[i] * 2          
            ligne[i+1] = 0                   
    return ligne
def deplacer_gauche(grille):
    for i in range(TAILLE):
        ligne = tasser(grille[i])
        ligne = fusionner(ligne)
        ligne = tasser(ligne)  #pour enlever les zeros restant 
        grille[i] = ligne


def deplacer_droite(grille):
    for i in range(TAILLE):
        ligne = tasser(grille[i][::-1])  # on tasse la ligne inversée
        ligne = fusionner(ligne)          
        ligne = tasser(ligne)             
        grille[i] = ligne[::-1]           # on remet la ligne à l'endroit 
def deplacer_haut(grille):
    for j in range(TAILLE):          # pour chaque colonne
        colonne = []
        for i in range(TAILLE):      # on extrait la colonne
            colonne.append(grille[i][j])
        colonne = tasser(colonne)    # on tasse vers le haut
        colonne = fusionner(colonne) 
        colonne = tasser(colonne)    
        for i in range(TAILLE):      # on remet dans la grille
            grille[i][j] = colonne[i]
def deplacer_bas(grille):
    for j in range(TAILLE):
        colonne = []
        for i in range(TAILLE):
            colonne.append(grille[i][j])
        colonne = colonne[::-1]      # on retourne
        colonne = tasser(colonne)
        colonne = fusionner(colonne)
        colonne = tasser(colonne)
        colonne = colonne[::-1]      # on re retourne
        for i in range(TAILLE):
            grille[i][j] = colonne[i]


