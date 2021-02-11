#groupe MIASHS TD1
#Margaux Ulliac
#Sulayman Charpentier
#madjoua Djeti
#Fouad Abdoullah
#https://github.com/uvsq22000868/projet_incendie


import tkinter as tk

#on crée la fenêtre sur laquelle seront les parcelles avec l'incendie
HEIGHT=400
WIDTH=600
root= tk.Tk()
canvas= tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='white')

canvas.grid(column=0, row=0)
root.mainloop()

#on insère le quadrillage


#On insère le bouton qui va situer aléatoirement les parcelles d'eau, de forêt et de prairie.
