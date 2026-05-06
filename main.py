from grille import initialiser_grille, afficher_grille, ajouter_tuile, calculer_score
from Mouvement import deplacer_gauche, deplacer_droite, deplacer_haut, deplacer_bas
from conditionreussite import partie_perdue, partie_gagnee
import tkinter as tk
from interface import creer_fenetre, creer_cellules, mettre_a_jour, afficher_fin

# --- Initialisation du jeu ---
grille = initialiser_grille()
ajouter_tuile(grille)
ajouter_tuile(grille)

# --- Création de la fenêtre ---
fenetre = creer_fenetre()

label_score = tk.Label(fenetre, text="Score : 0", font=("Helvetica", 18, "bold"))
label_score.grid(row=0, column=0, columnspan=4, pady=10)

cellules = creer_cellules(fenetre)
mettre_a_jour(cellules, grille, label_score, calculer_score(grille))

# --- Fonction appelée à chaque touche ---
def jouer(event):
    if event.keysym == "Left":
        deplacer_gauche(grille)
    elif event.keysym == "Right":
        deplacer_droite(grille)
    elif event.keysym == "Up":
        deplacer_haut(grille)
    elif event.keysym == "Down":
        deplacer_bas(grille)
    else:
        return

    ajouter_tuile(grille)
    mettre_a_jour(cellules, grille, label_score, calculer_score(grille))

    if partie_gagnee(grille):
        afficher_fin(fenetre, "🎉 Tu as gagné !")
    if partie_perdue(grille):
        afficher_fin(fenetre, "💀 Game Over !")

# --- Lier les touches fléchées ---
fenetre.bind("<Left>",  jouer)
fenetre.bind("<Right>", jouer)
fenetre.bind("<Up>",    jouer)
fenetre.bind("<Down>",  jouer)

# --- Lancer la fenêtre ---
fenetre.mainloop()