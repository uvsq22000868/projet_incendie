import tkinter as tk
import random as rd

def quadrillage() :
    """Créer un terrain contenant plusieurs parcelles"""
    couleurs=["green", "orange red", "yellow"]
    #variables
    HEIGHT = 400
    WIDTH = 600
    largeur_case = WIDTH // 20
    hauteur_case = HEIGHT // 20
    couleur_fond = rd.choice(couleurs) #choisis une couleur aléatoirement dans la liste couleur
    #création du canvas(terrain)
    canvas = tk.Canvas(root, bg="red", height=HEIGHT, width=WIDTH)
    canvas.grid()
    #division du terrain en parcelles
    for i in range(21):
        for j in range(21) :
            if (i+j) % 2 != 0 :
                couleur_fond = rd.choice(couleurs)
            else:
                couleur_fond = "blue"
            parcelle= canvas.create_rectangle((i*largeur_case, j*hauteur_case),
                ((i+1)*largeur_case, (j+1)*hauteur_case), fill=couleur_fond)
            if couleur_fond == "orange red" :
                couleurs.remove(couleur_fond)

    def clic(event) :
        """Change l'état de la parcelle lorsque l'utilisateur fait un clic gauche"""
        x= event.x 
        y= event.y
        if x < 600 :
            canvas.itemconfigure(parcelle, fill="orange red")
            pass
        #pas terminé
    canvas.bind("<Button-1>", clic)

#####programme principal######
root=tk.Tk()
#bouton_terr= tk.Button(root, text="Terrains", font=("Times, 30"), bg="White", command=quadrillage)
quadrillage()
#bouton_terr.grid(column=1, padx="15cm", row=1)
root.mainloop()