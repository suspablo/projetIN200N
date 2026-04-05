from grille import TAILLE

# Vérifie si le joueur a perdu : grille pleine et aucune fusion possible
def partie_perdue(grille):
    for i in range(TAILLE):
        for j in range(TAILLE):
            if grille[i][j] == 0:
                return False
            if i < TAILLE - 1 and grille[i][j] == grille[i + 1][j]:
                return False
            if j < TAILLE - 1 and grille[i][j] == grille[i][j + 1]:
                return False
    return True

# Vérifie si le joueur a gagné : une case contient 2048
def partie_gagnee(grille):
    for i in range(TAILLE):
        for j in range(TAILLE):
            if grille[i][j] == 2048:
                return True
    return False