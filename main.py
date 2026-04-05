import random

TAILLE = 4

def initialiser_grille():  # crée une grille 4x4 remplie de zéros
    return [[0 for j in range(TAILLE)] for i in range(TAILLE)]

def afficher_grille(grille):# affiche la grille dans la console
    for ligne in grille:
        print(ligne)

def ajouter_tuile(grille):# ajoute une tuile (2 ou 4) à une position aléatoire de la grille
    cases_vides = []
    for i in range(TAILLE):
        for j in range(TAILLE):
            if grille[i][j] == 0:
                cases_vides.append((i, j))

    if cases_vides: # s'il y a des cases vides, en choisit une au hasard et y place une tuile
        i, j = random.choice(cases_vides)
        grille[i][j] = 4 if random.randint(0, 9) == 0 else 2
        return i, j
    return None

def partie_perdue(grille): # vérifie si le joueur a perdu : grille pleine et aucune fusion possible
    for i in range(TAILLE):
        for j in range(TAILLE):
            if grille[i][j] == 0:
                return False
            if i < TAILLE - 1 and grille[i][j] == grille[i + 1][j]:
                return False
            if j < TAILLE - 1 and grille[i][j] == grille[i][j + 1]:
                return False
    return True

def calculer_score(grille): # additionne toutes les valeurs de la grille pour calculer le score
    score = 0
    for i in range(TAILLE):
        for j in range(TAILLE):
            score += grille[i][j]
    return score

grille = initialiser_grille()
ajouter_tuile(grille)
afficher_grille(grille)