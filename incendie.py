#groupe MIASHS TD1
#Margaux Ulliac
#Sulayman Charpentier
#madjoua Djeti
#https://github.com/uvsq22000868/projet_incendie

import tkinter as tk
HEIGHT=400
WIDTH=600
largeur_case = WIDTH // 4
hauteur_case = HEIGHT // 4

for i in range(5):
    for j in range(5):
        if (i+j) % 2 == 0:
            color = "gray80"
        else:
            color = "black"
        canvas.create_rectangle((i*largeur_case, j*hauteur_case),
                ((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)

root= tk.Tk()
canvas= tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='white')

canvas.grid(column=0, row=0)
root.mainloop()
