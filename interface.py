import tkinter as tk

# Dictionnaire associant les valeurs des tuiles à leurs couleurs de fond
COULEURS = {
    0:    "#cdc1b4",
    2:    "#eee4da",
    4:    "#ede0c8",
    8:    "#f2b179",
    16:   "#f59563",
    32:   "#f67c5f",
    64:   "#f65e3b",
    128:  "#edcf72",
    256:  "#edcc61",
    512:  "#edc850",
    1024: "#edc53f",
    2048: "#edc22e",
}

def creer_fenetre():
    """Crée et retourne la fenêtre tkinter."""
    fenetre = tk.Tk()
    fenetre.title("2048")
    return fenetre

def creer_cellules(fenetre):
    """Crée la grille de 4x4 labels et la retourne."""
    cellules = []
    for i in range(4):
        ligne = []
        for j in range(4):
            cell = tk.Label(fenetre, text="", font=("Helvetica", 28, "bold"),
                            width=4, height=2, bg="#cdc1b4")
            cell.grid(row=i+1, column=j, padx=5, pady=5)
            ligne.append(cell)
        cellules.append(ligne)
    return cellules

def mettre_a_jour(cellules, grille, label_score, score):
    """Rafraîchit l'affichage avec la grille actuelle."""
    for i in range(4):
        for j in range(4):
            val = grille[i][j]
            texte = str(val) if val != 0 else ""
            couleur = COULEURS.get(val, "#3c3a32")
            cellules[i][j].configure(text=texte, bg=couleur)
    label_score.configure(text="Score : " + str(score))
def afficher_fin(fenetre, message):
    """Affiche une fenêtre popup de fin de partie."""
    popup = tk.Toplevel(fenetre)
    popup.title("Fin de partie")
    popup.resizable(False, False)

    tk.Label(popup, text=message, font=("Helvetica", 24, "bold"),
             pady=20, padx=40).pack()

    tk.Button(popup, text="Quitter", font=("Helvetica", 14),
              command=fenetre.destroy).pack(pady=10)