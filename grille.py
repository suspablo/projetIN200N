

import random

TAILLE = 4

def initialiser_grille():
    return [[0 for j in range(TAILLE)] for i in range(TAILLE)]

def afficher_grille(grille):
    for ligne in grille:
        print(ligne)

def ajouter_tuile(grille):
    cases_vides = []
    for i in range(TAILLE):
        for j in range(TAILLE):
            if grille[i][j] == 0:
                cases_vides.append((i, j))

    if cases_vides:
        i, j = random.choice(cases_vides)
        grille[i][j] = 4 if random.randint(0, 9) == 0 else 2
        return i, j
    return None
def calculer_score(grille):
    score = 0
    for i in range(TAILLE):
        for j in range(TAILLE):
            score += grille[i][j]
    return score

