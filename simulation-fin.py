import tkinter as tk
from interface import creer_fenetre, creer_cellules, mettre_a_jour, afficher_fin

# Grille figée avec 2048 dedans
grille_gagnee = [
    [2048, 1024, 512, 256],
    [8,    16,   32,  128],
    [4,    2,    4,   8],
    [0,    0,    0,   2],
]

fenetre = creer_fenetre()

label_score = tk.Label(fenetre, text="Score : 9999",
                        font=("Helvetica", 18, "bold"))
label_score.grid(row=0, column=0, columnspan=4, pady=10)

cellules = creer_cellules(fenetre)
mettre_a_jour(cellules, grille_gagnee, label_score, 9999)

# Popup de victoire après 1 seconde
fenetre.after(1000, afficher_fin, fenetre, "🎉 Tu as gagné !")

fenetre.mainloop()