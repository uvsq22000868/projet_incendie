#groupe MIASHS TD1
#Margaux Ulliac
#Sulayman Charpentier
#madjoua Djeti
#Fouad Abdoullah
#Sihem MADMAR
#https://github.com/uvsq22000868/projet_incendie


from random import sample
from tkinter import *

COLORS=["cyan", "green2", "orange red", "gray42", "yellow2", "black"]


def generateur_case(p, n): # Fonction qui genere des carré vert et bleu aleatoirement
    units=[(line,col) for col in range(n) for line in range(n)]
    ntrees=int(n**2*p)
    trees=sample(units,ntrees)
    states=[[0]*n for _ in range(n)]
    for (i,j) in trees:
        states[i][j]=1
    return states


def fill(states): # fonction qui change la couleur des carré
    n=len(states)
    for line in range(n):
        for col in range(n):
            fill_cell(states, line, col)

def propagate(): # fonction qui propage le feu
    update_states(states)
    canvas.delete("all")
    fill(states)
    canvas.after(150, propagate)


def fill_cell(states, line, col): # fonction qui change la couleur des carré
        A=(unit*col, unit*line)
        B=(unit*(col+1), unit*(line+1))
        state=states[line][col]
        color=COLORS[state]
        canvas.create_rectangle(A, B, fill=color, outline='black')


def update_states(states): # fonction qui change l'etat des cellules ( mort ou vivante)
    n=len(states)
    to_fire=[]
    for line in range(n):
        for col in range(n):
            if states[line][col]==2:
                states[line][col]=3
                for (i, j) in voisins(n, line, col):
                    if states[i][j]==1:
                        to_fire.append((i, j))
    for (line,col) in to_fire:
        states[line][col]=2


def voisins(n, i, j): # fonction qui verifie si les carré autour son vivant ou non
    return [(a,b) for (a, b) in
            [(i, j+1),(i, j-1), (i-1, j), (i+1,j)]
            if a in range(n) and b in range(n)]



def bouton_lancer(): # bouton qui sert a lancer la simulation (pas encore fini)
    print("Lancer...")
    propagate()


def carre(): #fonction pour faire le quadrillage
    ligne_vert() # fonction pour faire les lignes verticales
    ligne_hor() # fonction pour faire les lignes horizontales
        
def ligne_vert():
    c_x = 0
    while c_x != largeur:
        canvas.create_line(c_x,0,c_x,longeur,width=1,fill='black')
        c_x+=c
        
def ligne_hor():
    c_y = 0
    while c_y != longeur:
        canvas.create_line(0,c_y,largeur,c_y,width=1,fill='black')
        c_y+=c


def click_gauche(event): # fonction qui change la case en rouge
    print("L'utilisateur a clické")
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    canvas.create_rectangle(x, y, x+c, y+c, fill='red')
    etat_cellule[x,y]=1 # rend la cellule morte 1 = morte 0 = vivante





# Variables
largeur = 400
longeur = 400
etat_cellule = {} # liste qui contient l'etat de toutes les cellules
c = 10 # taille des carré
p=0.62
n=50
unit=10

#Creation de la fenetre
fenetre = Tk()
fenetre.title("Projet Incendie")

#Creation des parcelles

canvas = Canvas(fenetre, width=largeur, height=longeur)
bouton = Button(fenetre,text="Lancer",bg="white",command=bouton_lancer)
bouton.pack(side=TOP)
        



canvas.bind("<Button-1>", click_gauche)
canvas.pack()
carre()


# foret aleatoire
states=generateur_case(p, n)


i=n//2
j=0
states[i][j]=2


#

fill(states)


fenetre.mainloop() 
