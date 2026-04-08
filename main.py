from grille import initialiser_grille, afficher_grille, ajouter_tuile, calculer_score
from Mouvement import deplacer_gauche, deplacer_droite, deplacer_haut, deplacer_bas
from  conditionreussite import partie_perdue, partie_gagnee

grille = initialiser_grille()
ajouter_tuile(grille)
ajouter_tuile(grille)
afficher_grille(grille)

while True:
    direction = input("Direction (z=haut, s=bas, q=gauche, d=droite) : ")

    if direction == 'q':
        deplacer_gauche(grille)
    elif direction == 'd':
        deplacer_droite(grille)
    elif direction == 'z':
        deplacer_haut(grille)
    elif direction == 's':
        deplacer_bas(grille)
    else:
        print("Touche invalide, utilise z/q/s/d")
        continue

    ajouter_tuile(grille)
    afficher_grille(grille)
    print("Score :", calculer_score(grille))

    if partie_gagnee(grille):
        print(" Tu as gagné !")
        break
    if partie_perdue(grille):
        print("Game over !")
        break
